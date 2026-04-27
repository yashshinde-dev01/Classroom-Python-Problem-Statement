file=open('Example.txt','r')
content=file.read()
lst=content.split()
print(content)
freq={};
for i in lst:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1;

print(freq) 
