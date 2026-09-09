from fastapi import FastAPI

app = FastAPI(title="fastapi-cream")

@app.get("/")
async def root():
    return {"name": "fastapi-cream", "tag": "FastAPI, in cream."}
