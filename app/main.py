from typing import List
from fastapi import FastAPI , HTTPException
import uvicorn
from fastapi_pagination import Page, add_pagination, paginate
from fastapi.middleware.cors import CORSMiddleware

from crud import Specialities,  Branches , getDocuments
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
    specialities = Specialities.getSpecialities()
    return specialities


# get branches of specialities
@app.get('/speciality/{id}/branches' , response_model=serializers.BranchesSerializer)
def get_branches(id : int):
    try:
        branches = Branches.getBranches(id)
        speciality = Specialities.getSpecificSpeciality(id)
        results = {"title": speciality.title, "items": branches}
        return results
    except:
        raise HTTPException(status_code=404, detail="Item not found")


@app.get('/branche/{id}/documnets' , response_model=serializers.DocumentsSerializer)
def get_documents(id : int):
    try:
        documents = getDocuments(id)
        branche = Branches.getSpecificBranche(id)
        results = {"title": branche.title, "items": documents}
        return results
    except:
        raise HTTPException(status_code=404, detail="Item not found")



add_pagination(app)
## RUN!!!
if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")