bike = {
    'brand':'bajaj',
    'model':'avenger',
    'year':'2019',
    'engine':"220cc"
}
SEARCH = input("Enter key to be searched: ")
if SEARCH in bike:
    print("Yes",SEARCH,"is in the bike dictionary")
else:
    print("No",SEARCH,"is in the bike dictionary")   