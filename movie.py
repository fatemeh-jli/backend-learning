from fastapi import FastAPI
from pydantic import BaseModel

appi = FastAPI()


class Movies(BaseModel):
    name: str
    director: str
    rating: float
    id: int
    
    
movies = [
    {"name": "inception", "director": "nolan", "rating": 8.8, "id": 10},
    {"name": "parasite", "director": "bong", "rating": 8.5, "id": 11},
    {"name": "the cow", "director": "mehrjui", "rating": 7.9, "id": 12},
    {"name": "separation", "director": "farhadi", "rating": 8.3, "id": 13},
]


@appi.get("/movies")
def allmovies():
    return movies

@appi.get("/{id}")
def WhichMovie(id: int):
    for movie in movies:
        if movie["id"] == id:
            return {"it's what you've been looking for" : movie}
    return{"the movie": "doesn't exist"}
        
        

@appi.post("/movies")
def addaMovie(newmovie: Movies):
    movies.append(newmovie.model_dump())
    return{"new movie added succefully": newmovie}
#in the first try i forgot about .model_dump



class UpdateMovies(BaseModel):
    name: str      | None = None
    director: str  | None = None
    rating: float  | None = None
    id: int        | None = None
    

@appi.put("/movies/{id}")
def updated(id: int, updatedmovie: UpdateMovies):
    for movie in movies:
        if movie["id"] == id:
            movie.update(updatedmovie.model_dump(exclude_unset=True))
            
            return {"the book has updated": updatedmovie}
    return{"the movie": "doesn't exist"}