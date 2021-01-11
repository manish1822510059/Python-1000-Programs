def binary_search(list,item):
    first = 0
    last = len(list)-1
    found = False
    while(first<=last and not found):
        mid = (first+last)//2
        if list[mid] == item:
            found = True
        else:
            if item<list[mid]:
                last = mid-1
            else:
                first = mid +1
    return found                    








numlist = [4,12,45,78,87,56,20,2,3,44]
print('list has the items: ',numlist)
searchnum = int(input("Enter a number to Search for. :"))
found = binary_search(numlist,searchnum)
if found == True:
    print(searchnum,"is Present in the list")
else:
    print(searchnum,"is not Present in the list")
