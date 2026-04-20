#WAP to read special symbols from file.
f1=open("C:\\Users\\Prathamesh\\OneDrive\\Desktop\\Language\\Python\\150.txt","r")
s=f1.read() 
for i in s:
    if not i.isalnum() and not i.isspace():
        print(i)