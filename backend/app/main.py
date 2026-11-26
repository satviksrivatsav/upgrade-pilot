from fastapi import FastAPI

app = FastAPI(title="Upgrade Pilot v1.0.0", 
              description="A simple API for the Upgrade Pilot", 
              version="1.0.0")

@app.get("/health")
async def health_check() -> dict[str, str]:
    "Health check endpoint"
    return {"status": "healthy"}