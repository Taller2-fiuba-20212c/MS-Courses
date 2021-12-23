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
from models.examResolution import ExamResolution
from models.unit import Unit
from bson import ObjectId
import json

app = FastAPI()


@app.get("/courses")
async def getCourses(skip: int = 0, limit: int = 0):
    coursesList = coursesEntity((connection.db.courses.find().skip(skip).limit(limit)))
    headers = {"X-Total-Count": str(connection.db.courses.count_documents({})).encode("utf-8").decode("utf-8") }
    content = jsonable_encoder(coursesList)
    return JSONResponse(content=content, headers=headers)

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
    connection.db.courses.find_one_and_update({"_id": ObjectId(id)}, {"$set": course.dict()})
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

@app.put("/courses/{id}/removeTeacher")
async def removeTeacher(id: str, teacherId: str):
    connection.db.courses.find_one_and_update({"_id": ObjectId(id)}, {"$pull": {'teachers': teacherId}})
    return courseEntity(connection.db.courses.find_one({"_id": ObjectId(id)}))

@app.put("/courses/{id}/removeCollaborator")
async def removeCollaborator(id: str, collaboratorId: str):
    connection.db.courses.find_one_and_update({"_id": ObjectId(id)}, {"$pull": {'collaborators': collaboratorId}})
    return courseEntity(connection.db.courses.find_one({"_id": ObjectId(id)}))

@app.put("/courses/{id}/removeStudent")
async def removeStudent(id: str, studentId: str):
    connection.db.courses.find_one_and_update({"_id": ObjectId(id)}, {"$pull": {'students': studentId}})
    return courseEntity(connection.db.courses.find_one({"_id": ObjectId(id)}))

@app.get("/searchCoursesByCountryAndCategory")
async def searchCoursesByCountryAndCategory(country: str = ".", category: str = ""):
    if (not category):
        return coursesEntity(connection.db.courses.find({"country": {"$regex": country, "$options": "i"}, "published": True}))
    else:
        categories = category.split(",")
        return coursesEntity(connection.db.courses.find({"country": {"$regex": country, "$options": "i"}, "published": True, "category": {"$in": categories}}))

@app.get("/searchByText")
async def searchByText(randomText: str = "", suscription: str = "", category: str = ""):
    query = '[{"$match": {"published": true}}, {"$match": {"$or": [{"name": {"$regex": "' + randomText + '", "$options": "i"}}, {"description": {"$regex": "' + randomText + '", "$options": "i"}}]}}'

    if (suscription):
        query += ", " + '{"$match": {"suscriptionIncluded": "' + suscription + '"}}'
    if (category):
        categories = category.split(",")
        query += ", " + '{"$match": {"category": {"$in": ' + str(categories) + '}}}'
    
    query += ']'
    query = query.replace('\'', '"')
    
    pipeline = json.loads(query)
    
    return coursesEntity(connection.db.courses.aggregate(pipeline))

@app.get("/getTop5Courses")
async def getTop5Courses():
    query = '[{"$match": {"published": true}}, {"$addFields": {"numberOfStudents": {"$size": "$students"}}}, {"$sort": {"numberOfStudents": -1}}, {"$limit": 5}]'

    pipeline = json.loads(query)
    return coursesEntity(connection.db.courses.aggregate(pipeline))

@app.put("/courses/{id}/addUnit")
async def addUnit(id: str, unit: Unit):
    connection.db.courses.find_one_and_update({"_id": ObjectId(id)}, {"$push": {'units' : unit.dict()}})
    return courseEntity(connection.db.courses.find_one({"_id": ObjectId(id)}))

@app.put("/courses/{id}/addExam")
async def addExam(id: str, unitName: str, exam: ExamModel):
    connection.db.courses.find_one_and_update({"_id": ObjectId(id), "units": {"$elemMatch": {"name": unitName}}}, {"$set": {'units.$.exam': exam.dict()}})
    return courseEntity(connection.db.courses.find_one({"_id": ObjectId(id)}))

@app.put("/courses/{id}/addExamResolution")
async def addExamResolution(id: str, unitName: str, examResolution: ExamResolution):
    connection.db.courses.find_one_and_update({"_id": ObjectId(id), "units": {"$elemMatch": {"name": unitName}}}, {"$push": {'units.$.exam.examResolutions': examResolution.dict()}})
    return courseEntity(connection.db.courses.find_one({"_id": ObjectId(id)}))