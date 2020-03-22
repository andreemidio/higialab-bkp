from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {'message':'aooba'}

@app.post("/")
async def root():
    return {'message':'aooba'}


@app.put("/")
async def root():
    return {'message':'aooba'}

@app.delete("/")
async def root():
    return {'message':'aooba'}