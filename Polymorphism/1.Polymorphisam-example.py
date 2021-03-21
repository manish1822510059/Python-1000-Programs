class Duck:
    def quack(self):
        print("Quaaaaaaaaaaaaack")

    def feathers(self):
        print("the duck has white feathers")


class Person:
    def quack(self):
        print("The person can imitate duck")

    def feathers(self):
        print("the person takes a feather from ground and takes it")

    def name(self):
        print("Matt Henry")

def in_the_forest(obj):
    obj.quack()
    obj.feathers()

donald = Duck()
matt = Person()

in_the_forest(donald)

print("-------------------------")
in_the_forest(matt)





