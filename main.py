# main.py
"""
Diabetes Prediction API - MLOps Implementation
FastAPI application with model serving and monitoring
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import joblib
import numpy as np
import json
import os
from datetime import datetime
import uvicorn

# Initialize FastAPI app
app = FastAPI(
    title="Diabetes Prediction MLOps API",
    description="ML model serving with FastAPI for diabetes risk prediction",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global variables
model = None
model_metadata = None
prediction_count = 0

class DiabetesInput(BaseModel):
    """Input schema for diabetes prediction"""
    Pregnancies: int = Field(..., ge=0, le=20, description="Number of pregnancies")
    Glucose: float = Field(..., ge=50, le=300, description="Glucose level (mg/dL)")
    BloodPressure: float = Field(..., ge=40, le=150, description="Blood pressure (mmHg)")
    BMI: float = Field(..., ge=15, le=60, description="Body Mass Index")
    Age: int = Field(..., ge=18, le=100, description="Age in years")

class PredictionResponse(BaseModel):
    """Response schema for predictions"""
    diabetic: bool = Field(..., description="Diabetes risk prediction")
    probability: float = Field(..., description="Prediction probability")
    model_version: str = Field(..., description="Model version")
    timestamp: str = Field(..., description="Prediction timestamp")

def load_model():
    """Load the trained model and metadata"""
    global model, model_metadata
    
    try:
        # Load model
        if os.path.exists("diabetes_model.pkl"):
            model = joblib.load("diabetes_model.pkl")
            print("✅ Model loaded successfully")
        else:
            raise FileNotFoundError("Model file not found. Run train.py first.")
        
        # Load metadata
        if os.path.exists("model_metadata.json"):
            with open("model_metadata.json", "r") as f:
                model_metadata = json.load(f)
            print("✅ Model metadata loaded")
        else:
            model_metadata = {"version": "1.0", "model_type": "RandomForest"}
            
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        raise

# Load model on startup
@app.on_event("startup")
async def startup_event():
    """Initialize application"""
    print("🚀 Starting Diabetes Prediction API...")
    load_model()
    print("✅ API ready!")

@app.get("/")
async def root():
    """API information endpoint"""
    return {
        "message": "🏥 Diabetes Prediction MLOps API",
        "status": "active",
        "version": "1.0.0",
        "endpoints": {
            "predict": "/predict",
            "health": "/health", 
            "docs": "/docs"
        }
    }

@app.get("/health")
async def health_check():
    """Health check for monitoring"""
    return {
        "status": "healthy" if model is not None else "unhealthy",
        "model_loaded": model is not None,
        "prediction_count": prediction_count,
        "timestamp": datetime.now().isoformat()
    }

@app.get("/model-info")
async def get_model_info():
    """Get model information"""
    if model_metadata is None:
        raise HTTPException(status_code=503, detail="Model metadata not available")
    
    return {
        "model_metadata": model_metadata,
        "prediction_count": prediction_count
    }

@app.post("/predict", response_model=PredictionResponse)
async def predict_diabetes(data: DiabetesInput):
    """Make diabetes prediction"""
    global prediction_count
    
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    try:
        # Prepare input for prediction
        input_data = np.array([[
            data.Pregnancies,
            data.Glucose,
            data.BloodPressure,
            data.BMI,
            data.Age
        ]])
        
        # Make prediction
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0].max()
        
        # Update counter
        prediction_count += 1
        
        # Log prediction (in production, use proper logging)
        print(f"Prediction #{prediction_count}: {'Diabetic Risk' if prediction else 'Low Risk'} (confidence: {probability:.2f})")
        
        return PredictionResponse(
            diabetic=bool(prediction),
            probability=round(float(probability), 3),
            model_version=model_metadata.get("version", "1.0"),
            timestamp=datetime.now().isoformat()
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

@app.get("/stats")
async def get_stats():
    """Get API usage statistics"""
    return {
        "total_predictions": prediction_count,
        "model_info": model_metadata,
        "api_version": "1.0.0"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)