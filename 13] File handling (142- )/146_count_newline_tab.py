#WAP to count number of new line, number of tabs in file
f1=open("C:\\Users\\Prathamesh\\OneDrive\\Desktop\\Language\\Python\\146.txt","r")
s=f1.read()
newline_count = s.count('\n') 
tab_count = s.count('\t')
print(s)

print("Number of new lines:", newline_count)
print("Number of tabs:", tab_count)