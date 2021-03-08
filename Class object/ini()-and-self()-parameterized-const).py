class VotingVote:
    def __init__(self,eligibleAge):
        self.eligiableAge = eligibleAge


    def isEligible(self,user_age):
        if user_age>=self.eligiableAge:
            print("Your are Eligiable for voting")
        else:
            print("your are NOT Eligiable for Voting") 



v1 = VotingAge(18)
v1.isEligible(25)  

v2 = VotingAge(16)
v2.isEligible(14)  


        