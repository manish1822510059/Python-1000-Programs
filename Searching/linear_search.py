numlist = [4,12,7,45,52,71,55]
print("List has the items:",numlist)
searchnum = int(input("Enter a number to search for:"))
found = False
for  i in range(len(numlist)):
    if numlist[i]==searchnum:
        found = True
        print(searchnum,' is Present in the List at index',i)
        break

if found==False:
    print(searchnum,'is Not Found in the List')    
