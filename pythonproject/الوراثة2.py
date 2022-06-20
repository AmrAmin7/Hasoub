class Employee:

    total=0
    __salary_raise=1.1

    def __init__(self,first_name,last_name,salary):
        self.first_name= first_name
        self.last_name= last_name
        self.salary = salary
        Employee.total+=1

    def info(self):
        return f'Name:{self.first_name} {self.last_name}'

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

class Manager(Employee):
    def __init__(self,first_name,last_name,salary,employees):
        super().__init__(first_name,last_name,salary)
        self.employees = employees



    def get_employees(self):
        print("Employees:")
        print("="*10)
        employees_list=[]
        for number,employee in enumerate (self.employees):
            employees_list.append(f"{number+1}.{employee.info()}")
        return '\n'.join(employees_list)

class Programmer(Employee):
    def __init__(self,first_name,last_name,salary,lang,projects):
        super().__init__(first_name,last_name,salary)
        self.lang=lang
        self.projects=projects
    def get_projects(self):
        print("Projects:")
        print("="*10)
        projects_list=[]
        for number,project in enumerate (self.projects):
            projects_list.append(f"{number+1}.{project.info}")
        return '\n'.join(projects_list)
class Projects():
    def __init__(self,name,describtion,day,done,info):
        self.name=name
        self.describtion=describtion
        self.day=day
        self.done=done
        self.info=info
project1=Projects('Project1','Old',5,True,'test')
project2=Projects('Project2','New',7,False,'test1')
amr = Programmer('Amr','Amin',4500,'Python',[project1,project2])
print(amr.info())
print(amr.get_projects())
