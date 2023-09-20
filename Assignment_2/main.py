import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)#####
cashier_instance = Cashier()######




def main():
    ###  write the rest of the codes ###
    coins = 0
    userchoice = ''
    while (1):  # continues to loop until user chooses off option
        userchoice = input(
            "What would you like? (small/medium/large/off/report): ")  # ask user for their input and takes it
        userchoice = userchoice.lower()  # ensures all input is lowercase
        if (userchoice == 'off'):  # if user input is off sets x to 5 kills loop program ends
            break

        if (userchoice == 'report'):  # prints report
            print(resources)
            continue

        if (sandwich_maker_instance.check_resources(
                recipes[userchoice]["ingredients"]) == 'False'):  # checks if there are resources for the user's choice
            continue

        coins = cashier_instance.process_coins()  # handles the coin inputting

        if (cashier_instance.transaction_result(coins, recipes[userchoice][
            "cost"]) == 'true'):  # checks if the user has inputted enough money
            sandwich_maker_instance.make_sandwich(userchoice,
                              recipes[userchoice]["ingredients"])  # if enough money was inserted makes sandwich
            continue

        else:
            print("Sorry, that’s not enough money. Money refunded.")  # not enough money refund, plus no sandwich making
            continue
if __name__=="__main__":
    main()
