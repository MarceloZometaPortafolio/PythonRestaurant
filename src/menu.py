class Menu:    
    __MenuList = {}

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

    def get_price_by_item(self, item):
        return self.MenuList[item]

    def add_item(self, item):
        for key in item:
            if not (key in self.MenuList):
                self.MenuList.update(item)