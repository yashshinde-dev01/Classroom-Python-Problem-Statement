#WAP to write some words in file and read vowels from the file
f1=open("C:\\Users\\Prathamesh\\OneDrive\\Desktop\\Language\\Python\\151.txt","w")
f1.write("Hello world")
f1.close()

f1=open("C:\\Users\\Prathamesh\\OneDrive\\Desktop\\Language\\Python\\151.txt","r")
s=f1.read()
for i in s:
    if i in "aeiouAEIOU":
        print(i)