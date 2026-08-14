from fastapi import FastAPI

app = FastAPI(
    title="Automated CI/CD Deployment Pipeline",
    description="A FastAPI service used to demonstrate an automated CI/CD deployment workflow.",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "DevOps Deployment Pipeline API",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }


@app.get("/api/status")
def api_status():
    return {
        "service": "devops-deployment-pipeline",
        "environment": "development",
        "status": "running",
    }