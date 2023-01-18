from database import SessionLocal
from models import Speciality , Branch , Document
from serializers import SpecialitySerializer

session = SessionLocal()

def getSpecialities():
    with session:
        return session.query(Speciality).all()

def getBranches(id):
    with session:
        return session.query(Branch).filter(Branch.speciality_id == id).all()

def getDocuments(id):
    with session:
        return session.query(Document).filter(Document.branch_id == id).all()