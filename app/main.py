# main.py

from typing import List, Optional
from fastapi import FastAPI, status, HTTPException, Response
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, HttpUrl
from config import connection
from schemas.course import courseEntity, coursesEntity
from models.course import Course
from models.examModel import ExamModel
from bson import ObjectId

app = FastAPI()


@app.get("/courses")
async def getCourses():
    return coursesEntity((connection.db.courses.find()))

@app.post("/courses")
async def createCourse(course: Course):
    new_course = jsonable_encoder(course)
    id = connection.db.courses.insert_one(new_course).inserted_id
    if id != None:
        return {"created": True, "id": str(id)}
    else:
        return {"created": False, "id": str(id)}

@app.get("/courses/{id}")
async def getCourseById(id: str):
    return courseEntity(connection.db.courses.find_one({"_id": ObjectId(id)}))

@app.put("/courses/{id}")
async def updateCourse(id: str, course: Course):
    connection.db.courses.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(course)})
    return courseEntity(connection.db.courses.find_one({"_id": ObjectId(id)}))

@app.delete("/courses/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def deleteCourse(id: str):
    connection.db.courses.find_one_and_delete({"_id": ObjectId(id)})
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/courses/{id}/addTeachers")
async def addTeachers(id: str, teacherIds: List[str]):
    connection.db.courses.find_one_and_update({"_id": ObjectId(id)}, {"$push": {'teachers' : {"$each" : teacherIds}}})
    return courseEntity(connection.db.courses.find_one({"_id": ObjectId(id)}))

@app.put("/courses/{id}/addCollaborators")
async def addCollaborators(id: str, collaboratorIds: List[str]):
    connection.db.courses.find_one_and_update({"_id": ObjectId(id)}, {"$push": {'collaborators' : {"$each" : collaboratorIds}}})
    return courseEntity(connection.db.courses.find_one({"_id": ObjectId(id)}))

@app.put("/courses/{id}/addStudents")
async def addStudents(id: str, studentIds: List[str]):
    connection.db.courses.find_one_and_update({"_id": ObjectId(id)}, {"$push": {'students' : {"$each" : studentIds}}})
    return courseEntity(connection.db.courses.find_one({"_id": ObjectId(id)}))

@app.get("/courses/{id}/getTeachers", response_model=List[str])
async def getTeachers(id: str):
    teachersJson = connection.db.courses.find_one({"_id": ObjectId(id)}, {'teachers' : 1, '_id': 0})
    return teachersJson['teachers']

@app.get("/courses/{id}/getCollaborators", response_model=List[str])
async def getCollaborators(id: str):
    collaboratorsJson = connection.db.courses.find_one({"_id": ObjectId(id)}, {'collaborators' : 1, '_id': 0})
    return collaboratorsJson['collaborators']

@app.get("/courses/{id}/getStudents", response_model=List[str])
async def getStudents(id: str):
    studentsJson = connection.db.courses.find_one({"_id": ObjectId(id)}, {'students' : 1, '_id': 0})
    return studentsJson['students']



