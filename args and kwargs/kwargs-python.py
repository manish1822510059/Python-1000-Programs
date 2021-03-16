#**kwagrs use for complex agrument like dictionary store string values
def func(**kwargs):
    for key, value in kwargs.items():
        print("{} : {} ".format(key,value))

dict = {"Manish":"Male","Rashmi":"Female"}

func(**dict)

