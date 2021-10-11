# main.py

from typing import List, Optional
from fastapi import FastAPI, status, HTTPException, Response
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, HttpUrl
from config.db import conn
from schemas.course import coursesEntity, coursesEntity
from models.course import Course
from bson import ObjectId

app = FastAPI()


@app.get("/courses", response_model=list[Course])
async def getCourses():
    return coursesEntity(conn.local.courses.find())

@app.post("/courses", response_model=str)
async def createCourse(course: Course):
    new_course = dict(course)
    id = conn.local.courses.insert_one(new_course).inserted_id
    return str(id)

@app.get("/courses/{id}", response_model=Course)
async def getCourseById(id: str):
    return courseEntity(conn.local.courses.find_one({"_id": ObjectId(id)}))

@app.put("/courses/{id}", response_model=Course)
async def updateCourse(id: int, course: Course):
    courseEntity(conn.local.courses.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(course)}))
    return courseEntity(conn.local.courses.find_one({"_id": ObjectId(id)}))

@app.delete("/courses/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def deleteCourse(id: str):
    courseEntity(conn.local.courses.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=status.HTTP_204_NO_CONTENT)