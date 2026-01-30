"""
A Python microservice
"""
from fastapi import FastAPI
import os

app = FastAPI(
    title="github-workflow-1769789887",
    description="A Python microservice",
    version="0.1.0"
)


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "Welcome to github-workflow-1769789887",
        "version": "0.1.0"
    }


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "service": "github-workflow-1769789887"
    }


@app.get("/hello")
async def hello():
    """Custom hello endpoint."""
    return {
        "message": "hello, welcome to my IDP"
    }


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", "8000"))
    uvicorn.run(app, host="0.0.0.0", port=port)
