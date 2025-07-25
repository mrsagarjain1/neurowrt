from fastapi import FastAPI
from pydantic import BaseModel
from router_agent import chain, run_on_router

app = FastAPI()

class Request(BaseModel):
    user_input: str

@app.post("/")
def query_router(req: Request):
    #cmd = chain.run(req.user_input)
    cmd = chain.invoke(input={"user_input": "tell me the lan ip"})
    result = run_on_router(cmd.content)
    return {"command": cmd.strip(), "result": result}