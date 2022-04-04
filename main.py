from fastapi import FastAPI
from tasks import add
app = FastAPI()

@app.get("/")
async def root():
    result = add.delay(1,2)
    print(result.ready())
    return {"message" : f"{result.get(timeout=25)}Hello World"}

