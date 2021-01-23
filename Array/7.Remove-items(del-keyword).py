import array as arr
numarr = arr.array('i',[10,20,30,40,50])
print("Array items:")
print(numarr)

del numarr[2]
print("\nArray items (after del):")
print(numarr)