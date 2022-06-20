class Employee:
    def __init__(self, first_name, last_name, title, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.salary = salary
    def change_salary(self, addition):
        self.salary = self.salary + addition
        return self.salary

ahmed = Employee('Ahmed' ,'Kamel' ,'Accountant',3000)
ali = Employee('Ali','Hasan','Archive',3200)

print(ahmed.salary)
ahmed.change_salary(500)
print(ahmed.salary)




