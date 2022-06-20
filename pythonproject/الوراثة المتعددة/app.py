from Employee import Employee
from Manager import Manager
from Roles import *
from Payments import *
from Programmer import Programmer,FreelancerProgrammer
# ytm damg el malafat el folder el ra2esi
from Profile import Profile


if __name__ =='__main__':
    #print(FreelancerProgrammer.__mro__)
    # l m3rfet tarteb el asnaf gwa el senf da

    #sara = FreelancerProgrammer('Sara','Mazen',200,5,'PHP',['IOS App'])
    #print(sara.info())
    #print(sara.calculate_salary())
    #sara.assign_project('iOS App')
    #print(sara.get_projects())

    Ahmed = Programmer('Ahmed','Kamal',3000,'Python',['Website,Blog'])
    AhmedProfile = Profile('Cairo','012','ahmed@gmail.com',False)
    Ahmed.Profile =AhmedProfile

    sara = FreelancerProgrammer('Sara','Mazen',200,5,'PHP',['IOS App'])


    #print(Ahmed.info())
    #print(sara.info())
    print(Ahmed.Profile)