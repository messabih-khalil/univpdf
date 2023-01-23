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


class BranchesSerializer(BaseModel):
    title : str
    items : list[BranchSerializer] = []

    class Config:
        orm_mode = True

class DocumentSerializer(BaseModel):
    title : str
    pdf_url : str

    class Config:
        orm_mode = True

class DocumentsSerializer(BaseModel):
    title : str
    items : list[DocumentSerializer] = []

    class Config:
        orm_mode = True