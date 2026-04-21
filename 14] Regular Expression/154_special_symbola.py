#using regular expression find out only special symbol from given string
import re
s="@prathamesh$"
pattern=r"\W"
print(re.findall(pattern,s))