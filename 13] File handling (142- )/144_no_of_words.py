#Write a Python program that takes a text file as input and returns the number of words of a given text file
f1=open("C:\\Users\\Prathamesh\\OneDrive\\Desktop\\Language\\Python\\144.txt","r")
s=f1.read()
t=s.split()
print(t)
count=0

for i in t:
    if i.isalpha():
        count+=1

print("number of words are :",count)
f1.close()

