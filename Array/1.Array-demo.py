import array
#integer array
arrint = array.array('i',[1,2,3,4,5])
#float array
arrfloat = array.array('f',[1.1,2.2,3.3,4.4,5.5,6.6])
#chararray
arrchar = array.array('u',['A','B','C','D','E'])

print("\n Integer Array:")
for x in range(len(arrint)):
    print(arrint[x])

print("\n Float Array:")
for x in range(len(arrfloat)):
    print("{0:2f}".format(arrfloat[x])) 


print("\n Char Array:")
for x in range(len(arrchar)):
    print(arrchar[x]) 




