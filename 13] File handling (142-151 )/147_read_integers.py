#WAP to read only integer numbers from file
f1=open("C:\\Users\\Prathamesh\\OneDrive\\Desktop\\Language\\Python\\144.txt","r")
s=f1.read()
t=s.split()
count=0
for i in t:
    if i.isdigit():
        count+=1
    
print(count)