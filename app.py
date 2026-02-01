from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI(title="Character Counter", version="v1")

class Health(BaseModel):
    ok: bool

class CharCountResponse(BaseModel):
    input: str
    char_count: int

@app.get("/health", response_model=Health)
def health():
    return {"ok": True}

@app.get("/v1/char-count", response_model=CharCountResponse)
def char_count(text: str = Query(..., description="Text to count characters for")):
    return {"input": text, "char_count": len(text)}
