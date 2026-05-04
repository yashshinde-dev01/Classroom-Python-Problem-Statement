'''.implement following program using multilevel inheritance
take student class having department name has static variable or class level variable and student name , roll no, percentage and marks of 3 subjects
take another class has get student info having get student info method 
take student details as 3rd class or final class having display method which will display student info along with percentage
'''

# class student:
#     department="Data Science"
    

# class student_info(student):
#     def input(self):
#         self.name=input("Enter name of student :")
#         self.roll=input("Enter roll no. :")
#         self.m1=int(input("Enter marks of first subject :"))
#         self.m2=int(input("Enter marks of second subject :"))
#         self.m3=int(input("Enter marks of third subject :"))
#         self.per=(self.m1+self.m2+self.m3)/3


# class studen_disp(student_info):
#     def display(self):
#         print("Student name :",self.name)
#         print("Student roll no. :",self.roll)
#         print("Student percentage :",self.per)
#         print("Student department :",self.department)

# obj=studen_disp()
# obj.input()
# obj.display()
#--------------------------------
class student:
    department="Data Science"
    

class student_info(student):
    def input(self):
        self.name=input("Enter name of student :")
        self.roll=input("Enter roll no. :")
        self.m1=int(input("Enter marks of first subject :"))
        self.m2=int(input("Enter marks of second subject :"))
        self.m3=int(input("Enter marks of third subject :"))
        self.per=(self.m1+self.m2+self.m3)/3


class studen_disp(student_info):
    def display(self):
        print("Student name :",self.name)
        print("Student roll no. :",self.roll)
        print("Student percentage :",self.per)
        print("Student department :",self.department)


data=[]
num=int(input("How many students are :"))
for i in range(num):
    print(f"Enter student {i+1} details ")
    obj=studen_disp()
    obj.input()
    data.append(obj)
    print("\t")

print("Student details are :")
for j in data:
    print("\t\t")
    j.display()