from dataclasses import dataclass


@dataclass
class Person:
    f_name: str
    l_name: str
    email: str

    def fullName(self):
        return f"{self.f_name} {self.l_name}"


@dataclass
class Customer(Person):
    num: str

    def get_num(self) -> str:
        return self.num


@dataclass
class Employee(Person):
    ssn: str

    def get_ssn(self) -> str:
        return self.ssn
