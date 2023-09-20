import data
recipes = data.recipes
class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        total = 0.00  # variable for total coins
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please enter coins")
        total += (1.00 * (float(input(
            "Please enter number of Whole dollar coins: "))))  # asks for number of dollar coins and does the multiplication to add it to the total to keep up the total
        total += (0.50 * (float(input("Please enter number of Half dollar coins: "))))
        total += (0.25 * (float(input("Please enter number of Quarters: "))))
        total += (0.05 * (float(input("Please enter number of Nickles: "))))
        return total  # returns the total which is a float

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        ##
        if (coins >= cost):  # retuns true if the amount of money inserted is greater than the cost
            coins -= cost  # removes the cost from the inputed coins
            print("Here is $%5.2f in change." % (coins))  # prints the change
            return 'true'
        return 'false'