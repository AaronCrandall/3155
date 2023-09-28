### Data ###
recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18, ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        if (ingredients["bread"] > self.machine_resources["bread"]): #checks if there is enough resources for the requested sandwich
            print("There is not enough bread for your selection")
            return 'False' #returns false if not enough resources
        if (ingredients["ham"] > self.machine_resources["ham"]):
            print("There is not enough ham for your selection")
            return 'False'
        if (ingredients["cheese"] > self.machine_resources["cheese"]):
            print("There is not enough cheese for your selection")
            return 'False'
        return 'True' #returns true if enough resources exist

    def process_coins(self):
        total = 0.00 #variable for total coins
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please enter coins")
        total += (1.00 * (float(input("Please enter number of Whole dollar coins: ")))) #asks for number of dollar coins and does the multiplication to add it to the total to keep up the total
        total += (0.50 * (float(input("Please enter number of Half dollar coins: "))))
        total += (0.25 * (float(input("Please enter number of Quarters: "))))
        total += (0.05 * (float(input("Please enter number of Nickles: "))))
        return total #returns the total which is a float

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if(coins >= cost): #retuns true if the amount of money inserted is greater than the cost
            coins -= cost #removes the cost from the inputed coins
            print("Here is $%5.2f in change." % (coins)) #prints the change
            return 'true'
        return 'false'

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        self.machine_resources["bread"] -= order_ingredients["bread"] #removes the used ingredients from the resources
        self.machine_resources["ham"] -= order_ingredients["ham"]
        self.machine_resources["cheese"] -= order_ingredients["cheese"]
        print("%s sandwich is ready. Bon appetit!" % sandwich_size) #prints that the 'size' sandwich has been made

### Make an instance of SandwichMachine class and write the rest of the codes ###
def main():
    coins = 0
    userchoice = ''
    SM1 = SandwichMachine(resources) #create the sandwich machine
    while(1): #continues to loop until user chooses off option
        userchoice = input("What would you like? (small/medium/large/off/report): ")# ask user for their input and takes it
        userchoice = userchoice.lower() #ensures all input is lowercase
        if (userchoice == 'off'): #if user input is off sets x to 5 kills loop program ends
            break

        if (userchoice == 'report'): #prints report
            print(resources)
            continue

        if (SM1.check_resources(recipes[userchoice]["ingredients"]) == 'False'): #checks if there are resources for the user's choice
            continue

        coins = SM1.process_coins() #handles the coin inputting

        if (SM1.transaction_result(coins,recipes[userchoice]["cost"]) == 'true'): #checks if the user has inputted enough money
            SM1.make_sandwich(userchoice,recipes[userchoice]["ingredients"]) #if enough money was inserted makes sandwich
            continue

        else:
            print("Sorry, that’s not enough money. Money refunded.") #not enough money refund, plus no sandwich making
            continue


if __name__ == '__main__':
    main()