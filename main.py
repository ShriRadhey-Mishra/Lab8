from fastapi import FastAPI
app = FastAPI()
import uvicorn


@app.get("/")
def read_root():
    return dict(name = "Shri Radhey Mishra", Location = "Deheradun")


@app.get("/{data}")
def read_root(data):
    return dict(hi = data, Location = "Deheradun")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=80, reload=True)