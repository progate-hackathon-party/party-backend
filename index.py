from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users")
async def root():
    return {"users": ["John", "Doe"]}

@app.post("/users")
async def root():
    return {"message": "User created successfully"}

@app.put("/users")
async def root():
    return {"message": "User updated"}

@app.delete("/users")
async def root():
    return {"message": "User deleted"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")