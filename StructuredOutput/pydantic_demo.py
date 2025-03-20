from pydantic import BaseModel, EmailStr, Field
from typing import Optional


# Pydantic is capable of type coercing, when needed (automatic conversion of data type)
class Student(BaseModel): 
    name: str = 'Vatsalya' # Default Value
    age: Optional[int] = None # Optional Value
    email: EmailStr # Email String (built-in datatype in Pydantic)
    cgpa: float = Field(gt = 0, lt=10)
    
new_stud = {'age': 17, 'email': 'abc@gmail.com', 'cgpa': 5}

student = Student(**new_stud)

print(student) 