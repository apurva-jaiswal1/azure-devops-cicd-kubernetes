from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/")
def root():
    return {"message": "DevOps project is running"}