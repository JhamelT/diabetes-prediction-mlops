# 🩺 Diabetes Prediction Model – Your First MLOps Project (FastAPI + Docker + K8s)

> 🎥 YouTube video for the project: **"Build Your First MLOps Project"**

This project helps you learn **Building and Deploying an ML Model** using a simple and real-world use case: predicting whether a person is diabetic based on health metrics. We’ll go from:

- ✅ Model Training
- ✅ Building the Model locally
- ✅ API Deployment with FastAPI
- ✅ Dockerization
- ✅ Kubernetes Deployment

---

## 📊 Problem Statement

Predict if a person is diabetic based on:
- Pregnancies
- Glucose
- Blood Pressure
- BMI
- Age

We use a Random Forest Classifier trained on the **Pima Indians Diabetes Dataset**.

---

## 🚀 Quick Start

### 1. Clone the Repo

```bash
git clone https://github.com/iam-veeramalla/first-mlops-project.git
cd first-mlops-project
```

### 2. Create Virtual Environment

```
python3 -m venv .mlops
source .mlops/bin/activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

## Train the Model

```
# 🏥 Diabetes Prediction MLOps Pipeline

A production-ready MLOps implementation showcasing DevOps best practices for machine learning deployment, featuring automated training, API serving, and containerized deployment.

## 🎯 Project Overview

This project demonstrates **MLOps fundamentals** with a focus on **DevOps engineering principles**:
- Machine learning model training and validation
- RESTful API development with FastAPI
- Containerization with Docker
- Infrastructure as Code practices
- CI/CD pipeline integration

**Perfect for**: Cloud engineers transitioning to MLOps, showcasing automation and deployment skills.

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Data Pipeline │───▶│  Model Training │───▶│   API Serving   │
│   (Python)      │    │  (scikit-learn) │    │   (FastAPI)     │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                                       │
                                                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  Containerized  │◀───│   Kubernetes    │◀───│     Docker      │
│   Deployment    │    │   Deployment    │    │   Container     │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **ML Framework** | scikit-learn | Model training and inference |
| **API Framework** | FastAPI | REST API with automatic documentation |
| **Containerization** | Docker | Application packaging and deployment |
| **Orchestration** | Kubernetes | Container orchestration and scaling |
| **Model Serving** | Uvicorn | ASGI server for production deployment |
| **Data Processing** | pandas, numpy | Data manipulation and preprocessing |

## ⚡ Quick Start

### 1. Environment Setup
```bash
# Clone repository
git clone https://github.com/JhamelThorne/diabetes-prediction-mlops.git
cd diabetes-prediction-mlops

# Create virtual environment
python -m venv .mlops
source .mlops/bin/activate  # Linux/Mac
# .\.mlops\Scripts\Activate.ps1  # Windows

# Install dependencies
pip install -r requirements.txt
```

### 2. Model Training
```bash
# Train the diabetes prediction model
python train.py
```
**Output**: Trained model (`diabetes_model.pkl`) + metadata (`model_metadata.json`)

### 3. API Deployment
```bash
# Start the FastAPI server
python main.py
# or
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

**Access Points**:
- 🏠 **API Home**: http://localhost:8000
- 📚 **Interactive Docs**: http://localhost:8000/docs
- 🔍 **Health Check**: http://localhost:8000/health

## 🐳 Docker Deployment

### Build and Run Container
```bash
# Build Docker image
docker build -t diabetes-mlops-api .

# Run container
docker run -p 8000:8000 diabetes-mlops-api

# Verify deployment
curl http://localhost:8000/health
```

## ☸️ Kubernetes Deployment

```bash
# Deploy to Kubernetes cluster
kubectl apply -f k8s-deploy.yml

# Check deployment status
kubectl get pods
kubectl get services

# Port forward for local access
kubectl port-forward service/diabetes-api 8000:80
```

## 🔧 API Usage Examples

### Health Check
```bash
curl http://localhost:8000/health
```

### Make Prediction
```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "Pregnancies": 2,
    "Glucose": 120.0,
    "BloodPressure": 70.0,
    "BMI": 25.5,
    "Age": 30
  }'
```

**Response**:
```json
{
  "diabetic": false,
  "probability": 0.234,
  "model_version": "1.0",
  "timestamp": "2025-08-08T21:30:00"
}
```

## 📁 Project Structure

```
diabetes-prediction-mlops/
├── 🤖 train.py              # Model training pipeline
├── 🚀 main.py               # FastAPI application
├── 📋 requirements.txt      # Python dependencies
├── 🐳 Dockerfile            # Container configuration
├── ☸️ k8s-deploy.yml       # Kubernetes deployment
├── 📊 model_metadata.json   # Model information (generated)
├── 🎯 diabetes_model.pkl    # Trained model (generated)
└── 📚 README.md             # Project documentation
```

## 🧪 Testing the API

### Interactive Testing
Visit `http://localhost:8000/docs` for Swagger UI testing interface.

### Sample Test Cases
| Scenario | Pregnancies | Glucose | BloodPressure | BMI | Age | Expected Result |
|----------|-------------|---------|---------------|-----|-----|----------------|
| Low Risk | 1 | 85 | 65 | 22.0 | 25 | `false` |
| Medium Risk | 3 | 120 | 75 | 28.5 | 35 | `false` |
| High Risk | 6 | 180 | 90 | 35.0 | 45 | `true` |

## 📈 DevOps Features

- **🔄 Automated Training**: Reproducible model training pipeline
- **📦 Containerization**: Docker-ready application packaging
- **🎛️ Health Monitoring**: Built-in health checks and metrics
- **📊 API Documentation**: Auto-generated OpenAPI specifications
- **🔧 Configuration Management**: Environment-based configuration
- **📝 Logging**: Structured logging for production monitoring

## 🚀 Production Considerations

### Scalability
- Kubernetes horizontal pod autoscaling
- Load balancer integration
- Database integration for prediction logging

### Security
- API authentication and rate limiting
- Model versioning and rollback capabilities
- Input validation and sanitization

### Monitoring
- Application metrics collection
- Model drift detection
- Performance monitoring dashboards

## 🤝 DevOps Best Practices Demonstrated

✅ **Infrastructure as Code**: Kubernetes manifests and Docker configuration  
✅ **API-First Design**: RESTful API with comprehensive documentation  
✅ **Containerization**: Docker best practices for ML applications  
✅ **Health Monitoring**: Production-ready health checks and metrics  
✅ **Configuration Management**: Environment-based configuration  
✅ **Automated Testing**: Model validation and API testing strategies  

## 📚 Technologies Demonstrated

**Cloud & DevOps Skills**:
- Container orchestration (Docker, Kubernetes)
- API development and documentation (FastAPI, OpenAPI)
- Infrastructure automation principles
- Monitoring and observability setup
- Production deployment patterns

**Data & ML Skills**:
- Machine learning pipeline development
- Model training, validation, and serving
- Data processing and feature engineering
- Model performance monitoring

## 👨‍💻 About

This project showcases the intersection of **DevOps engineering** and **machine learning operations**, demonstrating how to build production-ready ML systems with proper automation, monitoring, and deployment practices.

**Built by**: Jha'Mel Thorne  
**Focus**: Cloud Engineering & DevOps  
**LinkedIn**: [linkedin.com/in/jhamel-thorne](https://www.linkedin.com/in/jhamel-thorne/)

---

⭐ **Star this repo if you found it helpful for your MLOps journey!**

