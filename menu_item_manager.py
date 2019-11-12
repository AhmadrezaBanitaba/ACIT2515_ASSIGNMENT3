from abstract_menu_item import AbstractMenuItem
from menu_item_stats import MenuItemStats
from food import Food
from drink import Drink





class MenuItemManager:
  
    """ creates menu item manager """    
    def __init__(self, restaurant_name):
        self._restaurant_name= restaurant_name
        self._menu = []
        self._next_available_id = int(0)

    def add_menu_item(self, menu_item):
        """adds a menu item to the menu list"""   
        self._next_available_id = self._next_available_id + 1
        if menu_item not in self._menu:
            self._menu.append(menu_item)
            menu_item.set_id(self._next_available_id)
        
        return str(self._next_available_id)

    def menu_exist(self, id):
        for menu in self._menu:
            if menu.get_id() == id:
                return True

        return False


    def remove_menu_item(self, id):
        if self.menu_exist(id) is True:
            for menu_item in self._menu:
                if menu_item.get_id() is id:
                    self._menu.remove(menu_item)

    



    def get_by_id(self, id):
        for menu_item in self._menu:
            if menu_item.get_id() == id:
                return menu_item
    
    def get_all_by_type(self, item_type):
        menu_list = []
        for menu_item in self._menu:
            if menu_item.get_type() == item_type:
                menu_list.append(menu_item.to_dict())
        return menu_list                

        

    def get_all(self):
        menu_list = []
        for menu_item in self._menu:
                menu_list.append(menu_item.to_dict())
        return menu_list                
 

    def update(self, menu_item):
        id = menu_item.get_id()
        if self.menu_exist(id) is False:
            raise ValueError("id does not exist")
        for index, menu_item in enumerate(self._menu, 0):
            if menu_item.get_id() == id:
                break
        self._menu[index] = menu_item




    def get_menu_item_stats(self):

        """ gets menu item stats """
        total_num_menu_items = int(0)
        num_foods = int(0)
        num_drinks = int(0)
        avg_price_food= float(0)
        avg_price_drink = float(0)
        item_price= float(0)
        food_price_list = []
        drink_price_list = []

        for menu_item in self._menu:
            total_num_menu_items += 1
            if menu_item.get_type() == "food":
                num_foods += 1
            if menu_item.get_type() == "drink":
                num_drinks += 1

        for menu_item in self._menu:
            if menu_item.get_type() == "drink":
                item_price = menu_item.get_price()
                drink_price_list.append(item_price)
                avg_price_drink = sum(drink_price_list)/len(drink_price_list)
                



        for menu_item in self._menu:
            if menu_item.get_type() == "food":
                item_price = menu_item.get_price()
                food_price_list.append(item_price)
                avg_price_food = sum(food_price_list)/len(food_price_list)

        stats = MenuItemStats(total_num_menu_items,num_foods, num_drinks, avg_price_food, avg_price_drink)

        return stats







