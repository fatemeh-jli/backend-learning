from fastapi import FastAPI, Path #what i need from the lib 
from typing import Optional
from pydantic import BaseModel



app = FastAPI() #made a new motour / app is the VARIABLE we saved a sample of fastapi in taht 

students = {
    1: {  #1 is the key and what is in that is value
        "name": "john", 
        "age": 17,
        "year": "years 12"
    }
}


#request Body  BaseModel
class Student(BaseModel):
    name: str
    age: int
    year: str


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

@app.get("/") #if sb came in this / url... (Decorator) difining HTTP Method & the route
def index(): #run this function 
    return {"name":"First Data"} #return this json text to client

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(description="The ID of the student you want to view, lt=3")):
    return students[student_id]



#combine path & query arameters
@app.get("/get-by-name/{student_id}")
def get_student(*, student_id: int, name: Optional[str] = None, test: str):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "not found"}

@app.post("/create-student/{student_id}")
def creat_student(student_id : int, student : Student):
    if student_id in students:
        return {"Error": "Student exists"}
    
    students[student_id] = student
    return students[student_id]

@app.put ("/update-student/{student-id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    
    if student.name != None: 
        students[student_id].name = student.name
        
    if student.age != None:
        students[student_id].age = student.age
        
    if student.year != None:
        students[student_id].year = student.year
        
    return students[student_id]


@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    
    del students[student_id]  # حذف دانشجو از دیکشنری
    return {"Message": f"Student with ID {student_id} deleted successfully"}

# ای‌پی‌آی دریافت نام با اصلاح ساختار JSON
from fastapi import Path

@app.get("/get-name/{name}")
def get_user_name(name: str = Path(description="لطفاً نام خود را وارد کنید")):
    return {
        "your_name": name,
        "description": "add your name"
    }