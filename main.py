from fastapi import FastAPI
import uvicorn
from logic import add, sub

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello"}

@app.get("/add/{num1}/{num2}")
async def add(num1: int, num2: int):
    """Add two numbers together"""

    total = add(num1,num2)
    return {"total": total}

@app.get("/sub/{num1}/{num2}")
async def sub(num1: int, num2: int):
    """Sub two numbers"""

    total = sub(num1,num2)
    return {"total": total}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')