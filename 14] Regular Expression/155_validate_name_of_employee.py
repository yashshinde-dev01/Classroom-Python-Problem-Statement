#Validate the name of employee using regular expression
import re
name=input("Enter your full name :")
pattern=r"[A-Za-z ]+"
if re.match(pattern,name):
    print("Valid")
else:
    print("Invalid")