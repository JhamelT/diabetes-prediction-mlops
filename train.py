# train.py
"""
Diabetes Prediction Model Training Pipeline
Simple, clean MLOps implementation for demonstration
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import json
from datetime import datetime

def create_sample_data():
    """Create synthetic diabetes dataset for demonstration"""
    np.random.seed(42)
    n_samples = 1000
    
    # Generate realistic diabetes risk factors
    data = {
        'Pregnancies': np.random.randint(0, 15, n_samples),
        'Glucose': np.random.normal(120, 30, n_samples),
        'BloodPressure': np.random.normal(70, 15, n_samples),
        'BMI': np.random.normal(30, 8, n_samples),
        'Age': np.random.randint(18, 80, n_samples)
    }
    
    # Create realistic target based on medical correlations
    risk_score = (
        0.01 * data['Pregnancies'] +
        0.005 * np.maximum(data['Glucose'] - 100, 0) +
        0.01 * np.maximum(data['BMI'] - 25, 0) +
        0.005 * np.maximum(data['Age'] - 30, 0) +
        np.random.normal(0, 0.1, n_samples)
    )
    
    # Binary classification: top 25% as diabetic risk
    data['Diabetic'] = (risk_score > np.percentile(risk_score, 75)).astype(int)
    
    df = pd.DataFrame(data)
    
    # Ensure realistic medical ranges
    df['Glucose'] = np.clip(df['Glucose'], 60, 250)
    df['BloodPressure'] = np.clip(df['BloodPressure'], 50, 120)
    df['BMI'] = np.clip(df['BMI'], 15, 50)
    
    print(f"Dataset created: {len(df)} samples")
    print(f"Diabetes prevalence: {df['Diabetic'].mean():.1%}")
    
    return df

def train_model():
    """Train and evaluate the diabetes prediction model"""
    print("Starting MLOps training pipeline...")
    
    # Load data
    df = create_sample_data()
    
    # Prepare features
    features = ['Pregnancies', 'Glucose', 'BloodPressure', 'BMI', 'Age']
    X = df[features]
    y = df['Diabetic']
    
    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print(f"Training samples: {len(X_train)}")
    print(f"Test samples: {len(X_test)}")
    
    # Train Random Forest model
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        class_weight='balanced'
    )
    
    print("Training model...")
    model.fit(X_train, y_train)
    
    # Evaluate model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"Model Accuracy: {accuracy:.3f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    # Feature importance
    importance = dict(zip(features, model.feature_importances_))
    print("\nFeature Importance:")
    for feature, imp in sorted(importance.items(), key=lambda x: x[1], reverse=True):
        print(f"  {feature}: {imp:.3f}")
    
    # Save model
    joblib.dump(model, 'diabetes_model.pkl')
    print("\nModel saved as 'diabetes_model.pkl'")
    
    # Save model metadata for API
    metadata = {
        "model_type": "RandomForestClassifier",
        "features": features,
        "accuracy": float(accuracy),
        "training_date": datetime.now().isoformat(),
        "version": "1.0"
    }
    
    with open('model_metadata.json', 'w') as f:
        json.dump(metadata, f, indent=2)
    
    print("Training pipeline completed successfully!")
    return model

if __name__ == "__main__":
    train_model()