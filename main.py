from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def health_check():
    return "healthy"

