#Write a Python program to remove newline characters from a file.
f1=open("C:\\Users\\Prathamesh\\OneDrive\\Desktop\\Language\\Python\\143.txt","r")
s=f1.readlines()
new=[line.rstrip('\n') for line in s]
print(new)
f1.close()