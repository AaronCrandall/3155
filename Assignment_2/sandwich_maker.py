import data
recipes = data.recipes
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        #####
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

    def make_sandwich(self, sandwich_size, order_ingredients):
        ########
        self.machine_resources["bread"] -= order_ingredients["bread"]  # removes the used ingredients from the resources
        self.machine_resources["ham"] -= order_ingredients["ham"]
        self.machine_resources["cheese"] -= order_ingredients["cheese"]
        print("%s sandwich is ready. Bon appetit!" % sandwich_size)  # prints that the 'size' sandwich has been made