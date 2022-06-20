class Salary:
    def __init__(self,salary):
        self.salary=salary

    def calculate_salary(self):
        return self.salary

class HourlyPayment:
    def __init__(self,work_hour,hour_rate):
        self.work_hour = work_hour
        self.hour_rate = hour_rate

    def calculate_salary(self):
        return self.hour_rate * self.work_hour