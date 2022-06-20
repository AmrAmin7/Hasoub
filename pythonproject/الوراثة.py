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





ahmed=Employee('Ahmed','Kamal',3000)
ali=Employee('Ali','Ahmed',4000)
najwa=Employee('Najwa','Mohamed',4500)
anwer=Manager('Anwer','Khaled',5000,[ahmed,ali,najwa])

print(anwer.get_employees())
