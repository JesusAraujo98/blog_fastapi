from pydantic import BaseModel

class Book(BaseModel):
    title:str
    author:str
    year:int
    categories:list[str]
    description:list[str]
    opinion:list[str]
    rate:int

