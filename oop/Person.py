class Person:
    def __init__(self, age: int, height: float) -> None:
        self.age = age
        self.height = height

    # def __dict__(self):

    def get_age(self) -> int:
        return self.age

    def get_height(self) -> float:
        return self.height
