from typing import List
from fastapi import FastAPI
import uvicorn
from fastapi_pagination import Page, add_pagination, paginate
from fastapi.middleware.cors import CORSMiddleware

from crud import getSpecialities , getBranches , getDocuments
import serializers

# initialize app

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# get all specialty
@app.get('/specialities' , response_model=List[serializers.SpecialitySerializer])
def get_specialities():
    specialities = getSpecialities()
    return specialities


# get branches of specialities
@app.get('/speciality/{id}/branches' , response_model=Page[serializers.BranchSerializer])
def get_branches(id : int):
    branches = getBranches(id)
    return paginate(branches)

@app.get('/branche/{id}/documnets' , response_model=Page[serializers.DocumentSerializer])
def get_documents(id : int):
    documents = getDocuments(id)
    return paginate(documents)




add_pagination(app)
## RUN!!!
if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")