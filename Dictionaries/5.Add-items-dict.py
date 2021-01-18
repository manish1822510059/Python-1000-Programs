bike = {'brand':'Bajaj',
        'model':'Avenger',
        'Year':2019,
        'engine':'220cc'}

print("Bike Details:")
for x in bike.items():

    print(x)

bike['color'] ='jet Black'
print("\n Bike Details (After Modification):")
for x in bike.items():
    print(x)