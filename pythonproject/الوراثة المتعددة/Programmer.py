from Employee import Employee,Freelancer
from Roles import *
from Payments import *

class Programmer(Employee,ProgrammerRole,Salary):
    # Programmer mo4taq mon Employee
    def __init__(self,first_name,last_name,salary,lang,projects=None):
        Salary.__init__(self,salary)
        ProgrammerRole.__init__(self,lang,projects)
        super().__init__(first_name, last_name)
        self.__salary=salary
        self.lang= lang
        if projects is None:
            projects=[]
        self.projects = projects

    def info(self):
        return f"Name:({self.first_name} {self.last_name}; Job title:{self.__class__.__name__})"

    #def calculate_salary(self):
        #return self.__salary
    def calculate_salary(self):
        return Salary.calculate_salary(self)

    @classmethod
    def from_string(cls, string):
        frist_name, last_name, title, salary,lang = string.split('-')
        salary = int(salary)
        return cls(frist_name, last_name,salary,lang)

    # mohmet el tab3 da hwa esnad el m4ro3 ll programmer el 7ali
    def assign_project(self,project):
        self.projects.append(project)
        # elly 3mlnah enna adragna el m4ro3(project) dmn qaimat projects

    def get_projects(self):
        print("Project:")
        print("*"*10)
        projects_list=[]
        for number, project in enumerate (self.projects):
            #enumerate de 2mr ll trqem w bybd2 bl 0 bas hnzod 1 3ala number 3shan ybd2 b 1
            projects_list.append(f"{number+1}.{project}")
        return '\n' .join(projects_list)

#class FreelancerProgrammer(Freelancer,Programmer):
    #haza el senf ytmata3 b5asyt Employee,Freelancer
    #def __init__(self,frist_name,last_name,hour_rate,work_rate,lang,projects):
        #Freelancer.__init__(self,frist_name,last_name,hour_rate,work_rate)
        #super().__init__(frist_name,last_name,hour_rate,work_rate)

        #Programmer.__init__(self,frist_name,last_name,lang,projects)
        #super().__init__(first_name,last_name,lang,projects)

class FreelancerProgrammer(Employee,ProgrammerRole,HourlyPayment):
    def __init__(self,first_name,last_name,hour_rate,work_hour,lang,projects):
        HourlyPayment.__init__(self,work_hour,hour_rate)
        ProgrammerRole.__init__(self,lang,projects)
        Employee.__init__(self,first_name,last_name)

    def info(self):
        return f"Name:({self.first_name} {self.last_name}; Job title:{self.__class__.__name__}; Work Hour:{self.work_hour})"

    def calculate_salary(self):
        return Salary.calculate_salary(self)



