from flask import Flask, request
from food import Food
from drink import Drink
from abstract_menu_item import AbstractMenuItem
from menu_item_manager import MenuItemManager
import json
import os
from datetime import datetime

app = Flask(__name__)

menu_item_manager = MenuItemManager('D:/OOP/Assignment3/v1.2/test_menu.json')

# This is where the API methods will go
@app.route('/menu/menu_items', methods=['POST'])
def add_item():
    """ add a menu item """
    content = request.json
    try:
        for item in content:
            if content['type'] == 'food':
                menu_item = Food(content['menu_item_name'], content['menu_item_no'], (content['date_added']), content['price'],
                 content['calories'], content['cuisine_country'], content['main_ingredient'], content['portion_size'], content['is_vegetarian'])
    
            elif content['type'] == 'drink':
                menu_item = Drink(['menu_item_name'], ['menu_item_no'], ['date_added'], ['price'], ['calories'], ['manufacturer'], ['size'], ['is_fizzy'], ['is_hot'])


        menu_item_manager.add_menu_item(menu_item)

        response = app.response_class(
            response= str(menu_item.get_id()), 
            status= 200
        )
        
    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=400
        )

    return response



@app.route('/menu/menu_items/<string:id>', methods=['GET'])
def get_menu_item(id):
    """ returns a menu item based on the id"""

    try:

        if menu_item_manager.menu_exist(int(id)) is True:

            check =menu_item_manager.get_by_id(int(id))

            dict = check.to_dict()

            response = app.response_class(

                status=200,

                response=json.dumps(dict),

                mimetype='/application/json'

            )

        else:

            response = app.response_class(

                status=404,
                response='menu item with given id does not exist'

            )

    except ValueError as e:

        response = app.response_class(

            response='menu item is invalid',

            status=400

        )

    return response




@app.route('/menu/menu_items/all', methods=['GET'])
def get_all_menu_items():
    """ returns all menu items"""

    try:
        if True:

            check =menu_item_manager.get_all()

            
            response = app.response_class(

                status=200,

                response=json.dumps(check),

                mimetype='/application/json'

            )

        else:

            response = app.response_class(

                status=404,
                response='device with given serial number does not exist'

            )

    except ValueError as e:

        response = app.response_class(

            response='Device is invalid',

            status=400

        )

    return response




@app.route('/menu/menu_items/all/<string:type>', methods=['GET'])
def get_all_by_type(type):
    """ returns menu item based on type  """
    try:
        a =menu_item_manager.get_all_by_type(type)

        response = app.response_class(

            status=200,

            response=json.dumps(a),

            mimetype='/application/json'

        )

    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=400
        )

    return response



@app.route('/menu/menu_items/stats', methods=['GET'])
def get_repiarstats():
    """ returns menu statistics """
    try:
        stats = menu_item_manager.get_menu_item_stats()

        response = app.response_class(

            status=200,

            response=json.dumps(stats.to_dict()),

            mimetype='/application/json'

        )

    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=400
        )

    return response







@app.route('/menu/menu_items/<string:id>', methods = ['PUT'])
def edit_menu_item():
    """ edits a  menu item given the id"""
    pass
    




@app.route('/menu/menu_items/<string:id>', methods=['DELETE'])
def remove_menu_item(id):
    """ deletes a menu item based on the id """

    try:
        if menu_item_manager.menu_exist(int(id)) is True:

            menu_item_manager.remove_menu_item(int(id))  

            response = app.response_class(

                status=200
            )

        else:

            response = app.response_class(

                status=404,
                response='menu item with given id does not exist'


            )

    except ValueError as e:

        response = app.response_class(

            response= str(e),

            status='400'

        )

    return response

















if __name__ == "__main__":
    app.run()
