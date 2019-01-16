# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 14:57:57 2019

@author: harpal
"""

class Employee :
    def employeeDetails(self):
        self.name="Matthew"
        print("name= ", self.name)
        self.age=30
        print("Age=",self.age)
    
    def printEmployeeDetails(self):
        print("Printing in another method")
        print("Name: ",self.name)
        print("Age: ",self.age)
        
    @staticmethod
    def welcome():
         print("Welcome to our Org")
     
    def displayEmployeeDetails(self):
        print(self.name)

employee=Employee()

employee.employeeDetails()
#Employee.employeeDetails(employee)
employee.printEmployeeDetails()
employee.welcome() 
employee.displayEmployeeDetails() 

#here we dont have __init__ method 

class Employee :
    
    def __init__(self):
        self.name="mark"

   
    def displayEmployeeDetails(self):
        print(self.name)

employee=Employee()
employee.displayEmployeeDetails() 

print("*********************")

class Employee :
    def __init__(self,name):
        self.name=name
    def displayEmployeeDetails(self):
        print(self.name)

employee=Employee("harry")
employee.displayEmployeeDetails() 


"#################################################"

class Library:
    def __init__(self,listOfBooks):
        self.availableBooks=listOfBooks
    
    def displayAvailableBooks(self):
        print()
        print("Available Books :")
        for book in self.availableBooks:
            print(book)
    
    def lendBook(self):
        if requestedBook in self.availableBooks:
            print("You have now borrowed the book")
            self.availableBooks.remove(requestedBook)
        else:
             print("Sorry book not aailable")
             
    def addBook(self,returnedBook):
        self.availableBooks.append(returnedBook)
        print("you have returned book")
    
class Customer:
    def requestBook(self):
        print("Enter the name of books you would like to borrow")
        self.book=input()
        return self.book
    
    def returnBook(self):
        print("Enter the name of book which you are going to return")
        self.book=input()
        return self.book
        
    
    
library=Library(["Thinks and Grow rich","Who will cry when u die","for ne MoreDay"])
customer=Customer()

while True:
    print("Enter 1 to display the available books")
    print("Enter 2 to request for a book")
    print("Enter 3 to return a book")
    print("Enter 4 to exit")
    
    userChoice=int(input())
    if userChoice is 1:
        library.displayAvailableBooks()
    elif userChoice is 2:
        requestedBook=customer.requestBook()
    elif  userChoice is 3:
        returnBook=customer.returnBook()
        library.addBook(returnBook)
    elif userChoice is 4:
        quit()
        
        
        
