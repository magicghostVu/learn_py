from oop.Person import Person


class Student(Person):
    def get_age(self) -> int:
        return 0

    def go_school(self) -> str:
        # string: str = self.height
        return "goto school"
