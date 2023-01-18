from pydantic import BaseModel

class SpecialitySerializer(BaseModel):
    id: int
    title : str
    description: str | None = None

    class Config:
        orm_mode = True

class BranchSerializer(BaseModel):
    id: int
    title : str

    class Config:
        orm_mode = True

class DocumentSerializer(BaseModel):
    id: int
    title : str
    pdf_url : str

    class Config:
        orm_mode = True