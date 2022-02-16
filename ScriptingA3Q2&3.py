"""
        Question 2&3: This program will create multiple members that will hold
                        different information for the employees including their
                        name and title. It will then print out all the information
"""
class Employee():
    def __init__(self, firstName, lastName, ID_Number, department, title):
        self.firstName = firstName
        self.lastName = lastName
        self.fullName = self.firstName+' '+self.lastName
        self.email = self.firstName.lower()+'.'+self.lastName.lower()+'@company.com'
        self.ID_Number = ID_Number
        self.department = department
        self.title = title

    def __str__(self):
        return 'Name:{self.firstName} {self.lastName} ''ID:{self.ID_Number} ''Department:{self.department} ' 'Title:{self.title} ''Email:{self.email}'.format(self=self)

emp1 = Employee('Susan', 'Meyers','47899','Accounting','Vice President')
print(emp1)
emp2 = Employee('Mark', 'Jones', '39119','IT','Programmer')
print(emp2)
emp3 = Employee('Joy', 'Rogers','81774','Manufacturing','Engineering')
print(emp3)
