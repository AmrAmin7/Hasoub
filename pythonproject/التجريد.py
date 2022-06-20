import datetime
from math import floor
from abc import ABC,abstractmethod

class Employee(ABC):
    total=0
    __salary_raise=1.1

    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        Employee.total=+1
    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def calculate_salary(self):
        pass


    @classmethod
    @abstractmethod
    def from_string(cls,string):
        frist_name,last_name,title,salary = string.split('-')
        salary = int(salary)
        return cls(frist_name,last_name)

    @staticmethod
    def is_working(day):
        if day.weekday==4 or day.weekday==5:
            return False
        return True


class Manager(Employee):
    def __init__(self,first_name,last_name,salary,employees=None):
        #None m3naha an employees e5tyarya
        super().__init__(first_name, last_name)
        self.__salary=salary
        if employees is None:
            employees=[]
        self.employees = employees

    def get_employees(self):
        print("Employee:")
        print("*"*10)
        employees_list=[]
        for number, employee in enumerate (self.employees):
            #enumerate de 2mr ll trqem w bybd2 bl 0 bas hnzod 1 3ala number 3shan ybd2 b 1
            employees_list.append(f"{number+1}.{employee.info()}")
        return '\n' .join(employees_list)

    # e7na bn3raf el twab3 tani 3shan de wazefa m4tqa mn Employee w 34an e7na 5lena el twab3 de mograda

    def info(self):
        return f"Name:({self.first_name}{self.last_name}; Job title:{self.__class__.__name__})"
        #__class__.__name__ ll 7sol 3la esm el snf el 7aly elly hwa Manager

    def calculate_salary(self):
        return self.__salary

    @classmethod
    def from_string(cls, string):
        frist_name, last_name, title, salary = string.split('-')
        salary = int(salary)
        return cls(frist_name, last_name,salary)

class Programmer(Employee):
    # Programmer mo4taq mon Employee
    def __init__(self,first_name,last_name,salary,lang,projects=None):
        super().__init__(first_name, last_name)
        self.__salary=salary
        self.lang= lang
        if projects is None:
            projects=[]
        self.projects = projects

    def info(self):
        return f"Name:({self.first_name}{self.last_name}; Job title:{self.__class__.__name__})"

    def calculate_salary(self):
        return self.__salary

    @classmethod
    def from_string(cls, string):
        frist_name, last_name, title, salary,lang = string.split('-')
        salary = int(salary)
        return cls(frist_name, last_name,salary,lang)

    # mohmet el tab3 da hwa esnad el m4ro3 ll programmer el 7ali
    def assign_project(self,project):
        self.projects.append(project)
        # elly 3mlnah enna adragna el m4ro3(project) dmn qaimat projects
