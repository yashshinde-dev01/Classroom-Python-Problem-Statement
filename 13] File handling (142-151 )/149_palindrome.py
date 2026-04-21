#WAP to read palindrome string and number from file
f1=open("C:\\Users\\Prathamesh\\OneDrive\\Desktop\\Language\\Python\\149.txt","r")
s=f1.read()
t=s.split() 
for i in t:
    if i==i[::-1]:
        print(i)