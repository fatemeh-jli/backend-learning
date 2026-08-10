from fastapi import FastAPI

app = FastAPI()

students = {}

@app.get("/")
def home():
    return {"message": "Student API is running"}

@app.get("/students")
def get_all_students():
    return students

@app.post("/students/{student_id}")
def create_student(student_id: int, name: str, age: int):
    students[student_id] = {"name": name, "age": age}
    return students[student_id]

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"error": "Student not found"}
    del students[student_id]
    return {"message": f"Student {student_id} deleted"}