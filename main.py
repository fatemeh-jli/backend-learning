#ill create a book api from first
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    title: str
    author: str
    rating: float | None = None
    price: float
    id: int
    
books =[ {"title": "book2", "author": "berry2", "price": 2.5, "id": 2},
{"title": "booki3", "author": "berry3", "price": 3.5, "id": 3},
{"title": "booki4", "author": "berry4", "price": 4.5, "id": 4}]



@app.get("/books")
def getall():
        return books
    

@app.get("/books/{id}")
def checkbook(id: int):
    for book in books:
        if book["id"] == id:
            return{"book details": book}
    return{"the book": "doesnt exist"}
            

@app.post("/books")
def addbook(booki: Book):
    books.append(booki)
    print(type(books[0]), type(booki))
    return {"accepted": booki}

class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    rating: float | None = None
    price: float | None = None


@app.put("/books/{id}")
def updatebook(id: int, new: BookUpdate):
    for book in books:
        if book["id"] == id:
            book.update(new.model_dump(exclude_unset=True)) #model_dump converting pydantic model to python dict
            print(type(new))

            return{"this book has updated" : book}
    return {"book": "doesn't exist"}





@app.delete("/books/{id}")
def delete2books (id : int):
    for book in books:
        if book["id"] == id:
            books.remove(book)
            return{"this book has deleted" : book}
    return {"book": "doesn't exist"}



