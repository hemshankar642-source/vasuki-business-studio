from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Vasuki Business Studio API", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

class DraftRequest(BaseModel):
    prompt: str
    business_name: str | None = None

@app.get("/")
def root():
    return {"name": "Vasuki Business Studio API", "status": "online"}

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/ai/draft")
def draft(body: DraftRequest):
    business = body.business_name or "your business"
    return {"text": f"Professional draft for {business}: {body.prompt}"}
