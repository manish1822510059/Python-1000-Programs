bike = {
    'brand':'bajaj',
    'model':'avenger',
    'year':'2019',
    'engine':"220cc"
}
print("Bike details:")
for x in bike.items():
    print(x)


bike.pop('engine') 
print("\n Bike details (after removing items)")
for x in bike.items():
    print(x)