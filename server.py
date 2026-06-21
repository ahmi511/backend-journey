from fastapi import FastAPI

# This initializes your API application
app = FastAPI()

# This is a "Route" or "Endpoint". 
# When a user visits the root URL ("/"), it runs this function.
@app.get("/")
def read_root() -> dict:
    return {"message": "Hello World! My FastAPI server is live."}

# Let's add a second endpoint just for fun!
@app.get("/status")
def check_status() -> dict:
    return {"status": "Operational", "framework": "FastAPI", "developer": "ahmi511"}