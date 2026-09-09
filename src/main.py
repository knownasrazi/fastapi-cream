from fastapi import FastAPI

app = FastAPI(title="fastapi-clean")

@app.get("/")
async def root():
    return {"name": "fastapi-clean", "tag": "FastAPI, in clean."}
