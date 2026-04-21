#use regular expression pattern for mobile no. , email id , date of birth , aadhar card no. and validate input given by user

#Mobile no.
# import re
# num=input("Enter mobile no. :")
# pattern="[0-9]{10}"                     

# if re.fullmatch(pattern,num):           #re.match(r"^[0-9]{10}$)
#     print("valid")
# else:
#     print("Invalid")


#Email
# import re
# email=input("Enter email :")
# pattern2=r"^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]$"        #r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"        
# if re.match(pattern2,email):
#     print("valid")
# else:
#     print("Invalid")

#Aadhar card
# import re
# aadhar=input("Enter Aadhar card no. :")
# pattern3=r"^[0-9]{12}$"
# if re.match(pattern3,aadhar):
#     print("valid")
# else:
#     print("Invalid")

#Date of Birth
import re
dob=input("Enter dob(dd/mm/yyyy) :")
pattern4=r"^[0-9]{2}/[0-9]{2}/[0-9]{4}$"
if re.match(pattern4,dob):
    print("Valid")
else:
    print("Invalid")