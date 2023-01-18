from fastapi import FastAPI
import uvicorn

# initialize app

app = FastAPI()


# get all specialty
@app.get('/')
def message():
    return "hello"

## RUN!!!
if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")