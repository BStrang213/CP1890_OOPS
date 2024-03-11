from dataclasses import dataclass


@dataclass
class Person:
    f_name: str
    l_name: str
    email: str

    @property
    def fullName(self):
        name = [(f, l) for f in self.f_name for l in self.l_name]
        return name


@dataclass
class Customer(Person):
    num = int


@dataclass
class Employee(Person):
    ssn = int
