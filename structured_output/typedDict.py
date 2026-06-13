from typing import TypedDict

class person(TypedDict):
    name: str
    age: int

new: person = {'name':"manas",'age': 19}
print(new)