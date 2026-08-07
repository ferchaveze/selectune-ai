from fastapi import FastAPI

app = FastAPI(
    title="SelectuneAI",
    description="Agentic AI DJ powered by RAG and personalized music intelligence",
    version="0.1.0",
)


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "selectune-ai"
    }