# main.py

from typing import List, Optional
from fastapi import FastAPI, status, HTTPException, Response
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, HttpUrl
from config import connection
from schemas.course import courseEntity, coursesEntity
from models.course import Course
from models.image import Image
from bson import ObjectId

app = FastAPI()


@app.get("/courses", response_model=list[Course])
async def getCourses():
    return coursesEntity(connection.db.courses.find())

@app.post("/courses", response_model=str)
async def createCourse(course: Course):
    new_course = dict(course)
    id = connection.db.courses.insert_one(new_course).inserted_id
    return str(id)

@app.get("/courses/{id}", response_model=Course)
async def getCourseById(id: str):
    return courseEntity(connection.db.courses.find_one({"_id": ObjectId(id)}))

@app.put("/courses/{id}", response_model=Course)
async def updateCourse(id: str, course: Course):
    courseEntity(connection.db.courses.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(course)}))
    return courseEntity(connection.db.courses.find_one({"_id": ObjectId(id)}))

@app.delete("/courses/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def deleteCourse(id: str):
    courseEntity(connection.db.courses.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=status.HTTP_204_NO_CONTENT)