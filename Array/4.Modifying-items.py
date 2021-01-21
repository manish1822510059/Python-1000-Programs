import array as arr
numarr = arr.array('i',[10,20,30,40,50,60,70,80])
print("Array items:")
print(numarr)
#changing index 3 value
numarr[3] = 44
print('\n Array items (after modifing):')
print(numarr)
#changing 1st to 5th index values
numarr[1:5] = arr.array('i',[-8,-5,-6,-7])
print("\n Array items (after modifing in range ):")
print(numarr)