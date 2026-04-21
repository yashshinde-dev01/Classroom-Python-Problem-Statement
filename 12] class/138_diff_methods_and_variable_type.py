#to demonstrate diff. methods and variable types in class of python
class first:
    x=26                   #class variable
    def show(self):         #instance method
        print('This is instance method')

    def __init__(self):     #constructor
        print('This is constructor ')

    @staticmethod
    def display():          #static method
        print('This is static method')
    
    
a=first()                  #object of class first
a.show()                   
first.display()             
    
