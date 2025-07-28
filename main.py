from fastapi import FastAPI
from router_agent import chain, run_on_router
from pydantic import BaseModel

app = FastAPI() 

# Model for incoming data
class UserData(BaseModel):
    user_input: str


@app.post("/query") #This will be executed whenever an HTTP POST request is received at the /query endpoint of this API.
def query_router(req: UserData):
    cmd = chain.invoke(input={"user_input": req.user_input})
    cmd = cmd.content
    result = run_on_router(cmd)
    return {"command": cmd.strip(), "result": result.strip()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)