from fastapi import FastAPI

app = FastAPI(title="Upgrade Pilot v0.1.0", 
              description="A simple API for the Upgrade Pilot", 
              version="0.1.0")

@app.add_api_route