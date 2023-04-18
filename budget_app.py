"""
Created on Mon Apr 17 13:06:12 2023

@author: ily-cloudy
"""

class Category:
    def __init__(self, n):
        self.name = n
        self.ledger = []
    
    def get_balance(self):
        self.bal = 0.0
        for i in self.ledger:
            self.bal = self.bal + i["amount"]
        self.bal = float(self.bal)
        return self.bal
    
    def check_funds(self, value = 0.0):
        if value > self.get_balance():
            return False
        else:
            return True
    
    def deposit(self, value = 0.0, description = ""):
         self.ledger.append({"amount" : value, "description" : description}) 
         
    def withdraw(self, value = 0.0, description = ""):
        if self.check_funds(value) == True:  
            self.ledger.append({"amount" : - value, "description" : description})
            return True
        else:
            return False
        
    def transfer(self, value, destination):
        if self.check_funds(value) == False:
            return False
        else:
            self.withdraw(value, f"Transfer to {destination.name}")
            destination.deposit(value, f"Transfer from {self.name}")
            return True

    # bodge :3 
    def __str__(self):
        s = f"{self.name:*^30}"
        for i in self.ledger:
            amount = i["amount"]
            description = i["description"]
            s += "\n" + f"{description[:23]:<23}" + f"{amount:>7.2f}"  
        s += "\n" + f"Total: {self.get_balance()}"
        return s 
        
def create_spend_chart(categories):
    # parameters
    cat_totals = []
    index = []
    percentages = []
    
    # setting up category totals
    for i in categories:
        cat_totals.append(0)
        index.append(i.name)
        for j in i.ledger:
            if j["amount"] < 0:
                cat_totals[-1] -= j["amount"]
                
    # percentages
    total = sum(cat_totals)
    for i in cat_totals:
        percent = (i / total) * 100
        percentages.append(percent)
        
    # formatting output (i barely know how, but it works (i think))
    s = "Percentage spent by category\n"
    
    # creating percentage visuals
    for i in range(100, -10, -10):
        s += f"{i:3d}| " 
        for j in percentages:
            if j >= i:
                s += "o  "
            else:
                s += "   "
        s += "\n" 
    s += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    
    # adding category names 
    length = max([len(i) for i in index])
    for i in range(length):
        s += "     "
        for j in index:
            if i < len(j):
                s += j[i] + "  "
            else:
                s += "   "
        if i != length - 1:
            s += "\n"

    return s
