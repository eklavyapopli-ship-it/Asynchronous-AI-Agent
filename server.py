from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def root():
    return {"Server":'Server is up and running'}