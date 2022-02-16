"""
        Question 2&3: This program will create multiple members that will hold
                        different information for the employees including their
                        name and title. It will then print out all the information
"""
#Creating the employee class
class Employee():
#Defining the members of the class as information about the employees
    def __init__(self, firstName, lastName, ID_Number, department, title):
        self.firstName = firstName
        self.lastName = lastName
#Combines first and last name together to make the fullname
        self.fullName = self.firstName+' '+self.lastName
#Combines first and last name and makes them lower case to keep it in an email format
        self.email = self.firstName.lower()+'.'+self.lastName.lower()+'@company.com'
        self.ID_Number = ID_Number
        self.department = department
        self.title = title
#Defining the string function to print out the employee info in a easy to read way
    def __str__(self):
        return 'Name:{self.firstName} {self.lastName} ''ID:{self.ID_Number} ''Department:{self.department} ' 'Title:{self.title} ''Email:{self.email}'.format(self=self)
#Defining employee objects and printing them to the user
emp1 = Employee('Susan', 'Meyers','47899','Accounting','Vice President')
print(emp1)
emp2 = Employee('Mark', 'Jones', '39119','IT','Programmer')
print(emp2)
emp3 = Employee('Joy', 'Rogers','81774','Manufacturing','Engineering')
print(emp3)
