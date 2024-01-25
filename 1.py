path=input('Enter path, C:\\Folder\\'+'\n')
word='TODO:'
txt1=open(path+'test1.tasks','r',encoding="utf-8")
txt2=open(path+'test2.tasks','r',encoding="utf-8")
txt3=open(path+'out.txt','w')
v1=len(open(path+'test1.tasks','r').readlines())
v2=len(open(path+'test2.tasks','r').readlines())
i=0
j=0
k=0
array=[]
for i in range(v1):
    line1=txt1.readline()
    temp1=line1.find(word) 
    dec1 = line1[temp1:len(line1)]
    if dec1 != '\n':
        array.append(dec1)

for i in range(v2):
    line2=txt2.readline()
    temp2=line2.find(word)
    dec2 = line2[temp2:len(line2)]
    if dec2 != '\n':
        array.append(dec2)
txt1.close()
txt2.close()
array.sort()
v3=len(array)
for k in range(v3):
    dec3=array[k]
    print(dec3)
    txt3.write(dec3)
txt3.close()
print('End')
