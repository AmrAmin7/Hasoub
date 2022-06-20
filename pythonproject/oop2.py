class Employee:

    def __init__(self, first_name, last_name, title, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.salary= salary
    @property
    def info(self):
        return f'Name:{self.first_name} {self.last_name},Job title:{self.title},salary:{self.salary}'

ahmed =Employee('Ahmed','Mohamed','Acountant',3000)
print(ahmed.info)

def change_salary(self,addition):
    self.salary=self.salary+ addition
    return self.salary
ahmed.change_salary(500)
print(ahmed.salary)
