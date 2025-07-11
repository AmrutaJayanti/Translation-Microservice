from fastapi import FastAPI
from routes.translate import router as translate_router

app = FastAPI(title="Translation Microservice")

# Register API routes
app.include_router(translate_router)

@app.get("/health")
def health():
    return {"status": "ok"}