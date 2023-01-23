from sqlalchemy import Column, Integer, String , JSON , ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Speciality(Base):
    __tablename__ = "specialities"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)

    branches = relationship("Branch", back_populates="Speciality")


class Branch(Base):
    __tablename__ = "branches"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    speciality_id = Column(Integer, ForeignKey("specialities.id"))

    Speciality = relationship("Speciality", back_populates="branches")
    documents = relationship("Document", back_populates="branch")


class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    branch_id = Column(Integer, ForeignKey("branches.id"))
    pdf_url = Column(String, nullable=False)
    branch = relationship("Branch", back_populates="documents")
