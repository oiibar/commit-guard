from fastapi import FastAPI

app=FastAPI(title="Commit Guard API")

@app.get("/health")
def health():
    return{"status":"ok"}
