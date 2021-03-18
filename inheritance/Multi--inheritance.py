class CementDealer:
    def GetCementCost(self,quantity):
        return quantity*300


class IronDealer:
    def GetIronCost(self,quantity):
        return quantity*4500

class Builder(CementDealer,IronDealer):
    def GetTotalCost(self,cQ,iQ):
        c_cost = self.GetCementCost(cQ)
        i_cost = self.GetIronCost(iQ)
        total_cost = c_cost+i_cost
        return total_cost


cement = int(input("Enter Cement Quantity : "))
Iron = int(input("Enetr Iron Quantity : "))
b = Builder()
total_cost = b.GetTotalCost(cement,Iron)        

print("Total Cost:" ,total_cost)
