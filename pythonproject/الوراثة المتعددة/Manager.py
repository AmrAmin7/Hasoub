from Employee import Employee


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
