import datetime

class Employee:

    total=0
    __salary_raise=1.1

    def __init__(self,first_name,last_name,title,salary):
        self.first_name= first_name
        self.last_name= last_name
        self.title = title
        self.salary = salary
        Employee.total+=1

    def info(self):
        return f'Name:{self.first_name} {self.last_name},Job title:{self.title}'

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self,salary):
        if salary<=0:
            raise ValueError
        self.__salary =salary

    @classmethod
    def __change_raise (cls,amount):
        cls.salary_raise = amount


    @classmethod
    def from_string (cls,string):
        first_name,last_name,title,salary = string.split('-')
        salary =int(salary)
        return cls(first_name,last_name,title,salary)



    @staticmethod
    def is_workday(day):
        if day.weekday()== 4 or day.weekday==5 :
            return False
        return True

ahmed =Employee.from_string('Ahmed-Kamal-33-3000')

print(ahmed.salary)
ahmed.salary=4000
print(ahmed.salary)

