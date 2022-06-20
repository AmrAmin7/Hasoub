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
        self.Profile = None
    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def calculate_salary(self):
        pass


    @classmethod
    def from_string(cls,string):
        frist_name,last_name,salary = string.split('-')
        salary = int(salary)
        return cls(frist_name,last_name)

    @staticmethod
    def is_working(day):
        if day.weekday==4 or day.weekday==5:
            return False
        return True

class Freelancer(Employee):
    # da mozaf 5arg el company a7drnah l3mal wzefa m3yana
    def __init__(self,first_name,last_name,hour_rate,work_hour):
        Employee.__init__(self,first_name,last_name)
        #super().__init__(first_name, last_name)  3shan yares mon el sanf Employee 3ala tool
        self.hour_rate = hour_rate
        self.work_hour = work_hour

    def info(self):
        return f"Name:({self.first_name} {self.last_name}; Job title:{self.__class__.__name__}; Work Hour:{self.work_hour})"

    def calculate_salary(self):
        return self.hour_rate * self.work_hour
        # hna ana ba2olo en el salary bta3o = hour rate * work rate

    def from_string(cls,string):
        frist_name,last_name,hour_rate,work_hour = string.split('-')
        hour_rate,work_hour = int(hour_rate),int(work_hour)
        return cls(frist_name,last_name,hour_rate,work_hour)
