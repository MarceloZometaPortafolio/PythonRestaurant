class Menu:    
    MenuList = []

    def __init__(self):
        super().__init__()
        self.MenuList = {
            "Cheeseburger": 5.50, 
            "Double Stack Bacon Cheeseburger": 7.50,
            "Salad": 2.50
        }

    def get_menu(self):
        returnString = ""
        for food in self.MenuList:
            returnString += food + "\t\t$" + str(self.MenuList[food]) + "\n"
    
        print(returnString)
        return returnString