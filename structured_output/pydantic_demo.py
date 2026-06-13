from pydantic import BaseModel, EmailStr, Field #field is use to set constaint
from typing import Optional

class student(BaseModel):
    name : str = 'aditya'
    age: Optional[int] = None
    email: Optional[EmailStr] = None
    cgpa: float = Field(gt=0, lt=10,default=5, description='Cpga of the student in float')

new_student = {'name':'Manas','email':'manas@gmail.com', 'cgpa':9.21}
# new2 = {'age': 19}

stu = student(**new_student)
# stu2= student(**new2)

print(stu)
# print(stu2)

# print(stu['name']) # gives error because its a pydantic object

stu_dict = dict(stu)

print(stu_dict['name'])

stu_json = stu.model_dump_json()
print(stu_json)



