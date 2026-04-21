# Find out only iintegers from given string and written only even numbers from that integers
import re
text="hello 12 my 45 name 42 is 250706"
pattern="[0-9]+"
s=re.findall(pattern,text)

for i in s:
    if int(i)%2==0:
        print(i)