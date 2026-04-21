import re

pattern="[0-9]+"
text="hello my name is Prathamesh 123 45"

s=re.findall(pattern,text)
print(s)