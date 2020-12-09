from oop.Person import Person
from typing import List

from oop.Student import Student

r = Person(25, 1.75)
# age = r.get_age()
# print("age is", age)
lp: List[Person] = []
lp.append(r)
student = Student(23, 1.67)
lp.append(student)
height: float = student.get_height()
