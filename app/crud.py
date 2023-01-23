from database import SessionLocal
from models import Speciality , Branch , Document
from serializers import SpecialitySerializer

session = SessionLocal()

class Specialities:
    def getSpecialities():
        with session:
            return session.query(Speciality).all()

    def getSpecificSpeciality(id):
        return session.query(Speciality).filter(Speciality.id == id).first()




class Branches:

    def getBranches(id):
        with session:
            return session.query(Branch).filter(Branch.speciality_id == id).all()

    def getSpecificBranches(id):
        with session:
            return session.query(Branch).filter(Branch.speciality_id == id).first()

def getDocuments(id):
    with session:
        return session.query(Document).filter(Document.branch_id == id).all()