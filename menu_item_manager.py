from abstract_menu_item import AbstractMenuItem
from menu_item_stats import MenuItemStats
from food import Food
from drink import Drink
import json


class MenuItemManager:
  
    """ creates menu item manager """    
    def __init__(self, filepath):
        self._menu = []
        self._next_available_id = int(0)
        self._filepath = filepath
        # self._read_menu_from_file()
        if not isinstance(self._filepath, str):
            raise ValueError('filepath must be string')



    def add_menu_item(self, menu_item):
        """adds a menu item to the menu list"""   
        self._next_available_id = self._next_available_id + 1
        if menu_item not in self._menu:
            self._menu.append(menu_item)
            menu_item.set_id(self._next_available_id)
        self._write_menu_to_file()
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


    
                       


    def _write_menu_to_file(self):         

        # Open the file at _filepath for writing (overwrite, not append)
        # Create an empty temporary list
        # For each entity in the list of entities:
        # Convert the entity to a Python dictionary (i.e., to_dict) and add it to the temporary list
        # Serialize the temporary list to a JSON string
        # Write the JSON string to the file
        # Close the file
        f = open(self._filepath, 'w')
        temp_list = []
        for i in self._menu:
            dict = i.to_dict()
            temp_list.append(dict)
            serializer = json.dumps(temp_list)
            f.write(serializer)
        f.close()    



    def _read_menu_from_file(self):

        # Open the file at _filepath for reading
        # Read in the contents of the file
        # Close the file
        # Deserialize from a JSON string to Python primitives (a list of dictionaries, where each dictionary represents an entity)
        # For each dictionary in the list:
        # If the type corresponds to SpecificEntity1:
        # Create a new instance of SpecificEntity1 using the attributes in the dictionary and add it to the entities list
        # Else if the type corresponds to SpecificEntity2:
        # Create a new instance of SpecificEntity2 using the attributes in the dictionary and add it to the entities list
        # Else raise an exception because the type is not supported

        f = open(self._filepath, 'r')
        f.read()
        f.close()
        deserialize = json.loads(f)


        for i in deserialize:
            if i['type']=='food':
                new_food = Food(i["menu_item_name"], i["menu_item_no"], i["date_added"],
                i["price"],i["calories"],i["cuisine_country"],
                i["main_ingredient"],i["portion_size"],i["is_vegetarian"])
                self._menu.append(new_food)
            elif i['type'] == 'drink':
                new_drink = Drink(i["menu_item_name"], i["menu_item_no"], i["date_added"], i["price"], i["calories"],
                 i["manufacturer"], i["size"], i["is_fizzy"], i["is_hot"])
                self._menu.append(new_drink)
            else:
                raise Exception("type is not supported")
                    
                