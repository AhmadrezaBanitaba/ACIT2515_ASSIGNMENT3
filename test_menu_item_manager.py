import unittest
from unittest import TestCase
import inspect
from menu_item_manager import MenuItemManager
from food import Food
from drink import Drink
import datetime
from menu_item_stats import MenuItemStats
from unittest.mock import patch, mock_open


class Testmanager(unittest.TestCase):
    """ Unit tests for menu_item_managerr"""

    @patch('builtins.open', mock_open(read_data='')
    def setUp(self):
        """Set up for all the values"""
        self.logPoint()
        self.reading_manager = TemperatureReadingManager("temp_testresults.csv")
        
        self.kashmir_dosa = MenuItemManager("test_menu.json")
        self.barley_bread = Food("barley bread", 12, datetime.date(2018, 8, 8), 12.99, 149, "India", "Barley", "small", True)

        self.mango_lasi3 = Drink("mango lasis", 10, datetime.date(2017, 9, 12), 12.99, 80, "lasi producer ltd", 129.99,
                            False, False)

        self.undefined_value = None
        self.empty_value = ""

    def test_team(self):
        """ 010A: Valid Construction """

        self.logPoint()

        self.assertIsNotNone(self.kashmir_dosa, "Team must be defined")

    def test_add(self):
        """ 020A: Valid Add menu """

        self.logPoint()

        self.assertIsNotNone(self.barley_bread, "Food must be defined")

        self.kashmir_dosa.add_menu_item(self.barley_bread)
        self.assertEqual(len(self.kashmir_dosa.get_all()), 1, "Menu has one item")
        self.assertEqual(self.kashmir_dosa._next_available_id, 1, "Id must be one")

    def test_add_undefined(self):
        """020B: invalid add menu"""
        self.logPoint()

        undefined_menu = None
        with self.assertRaisesRegex(ValueError, 'menu_item cannot be undefined'):
            self.kashmir_dosa.add_menu_item(undefined_menu)

    def test_add_menu_already_exists(self):
        """ 020C: Invalid Add menu - Menu Already Exists """

        self.logPoint()

        self.assertEqual(len(self.kashmir_dosa.get_all()), 0, "Menu has no item")

        self.kashmir_dosa.add_menu_item(self.barley_bread)
        self.assertEqual(len(self.kashmir_dosa.get_all()), 1, " Menu must have 1 item")

        self.kashmir_dosa.add_menu_item(self.barley_bread)
        self.assertEqual(len(self.kashmir_dosa.get_all()), 1, "Menu must have 1 item")

    def test_remove_menu_item(self):
        """ 030A: Valid remove menu """

        self.logPoint()

        self.kashmir_dosa.add_menu_item(self.barley_bread)
        self.assertEqual(self.kashmir_dosa._next_available_id, 1, "Id must be one")

        menu = self.kashmir_dosa.get_by_id(1)

        self.assertEqual(menu.get_id(), 1)

        self.kashmir_dosa.remove_menu_item(1)
        self.assertEqual(len(self.kashmir_dosa._menu), 0, "Must have no menu item")

    def test_remove_notint_menu_id(self):
        """ 030B: Invalid id int """

        self.logPoint()
        asdf = "3"
        self.assertRaisesRegex(ValueError,"needs to be int" ,self.kashmir_dosa.remove_menu_item, asdf)

    def test_remove_invalid_menu_id(self):
        """030C: invalid remove parameter"""
        self.logPoint()

        self.assertRaisesRegex(ValueError, "id cannot be undefined", self.kashmir_dosa.remove_menu_item, self.undefined_value)
        self.assertRaisesRegex(ValueError, "id cannot be empty", self.kashmir_dosa.remove_menu_item, self.empty_value)

    def test_delete_non_existent_menu(self):
        """ 030C: Invalid Delete Menu item - No id existent """

        self.logPoint()

        self.kashmir_dosa.add_menu_item(self.barley_bread)

        menu = self.kashmir_dosa.get_by_id(1)

        self.assertEqual(menu.get_id(), 1)

        self.kashmir_dosa.remove_menu_item(4)
        self.assertEqual(len(self.kashmir_dosa._menu), 1, "menu must have one items")

    def test_get_by_id(self):
        """ 040A: Valid Get the menu wanted """

        self.logPoint()

        self.kashmir_dosa.add_menu_item(self.barley_bread)

        menu = self.kashmir_dosa.get_by_id(1)

        self.assertEqual(menu.get_price(), 12.99, "menu price needs to be 12.99")
        self.assertEqual(menu.get_menu_item_no(), 12, "Menu item number needs to be 12")

    def test_menu_exist(self):
        """050A: Valid menu exists"""
        self.logPoint()

        self.kashmir_dosa.add_menu_item(self.barley_bread)

        self.assertEqual(self.kashmir_dosa._next_available_id, 1, "Id must be one")

        self.assertTrue("needs to be true", self.kashmir_dosa.menu_exist(1))

    def test_get_all(self):

        """060A: Get all the menus"""
        self.logPoint()

        self.kashmir_dosa.add_menu_item(self.barley_bread)
        self.kashmir_dosa.add_menu_item(self.mango_lasi3)
        list_menus = self.kashmir_dosa.get_all()

        self.assertEqual(list_menus[0].get_menu_item_name(), "barley bread", "needs to be barley bread")
        self.assertEqual(list_menus[1].get_menu_item_no(), 10, "needs to be 10")

    def get_all_menu_item(self):

        self.logPoint()
        """070A: Get all the menu item"""
        self.kashmir_dosa.add_menu_item(self.barley_bread)
        self.kashmir_dosa.add_menu_item(self.mango_lasi3)

        self.assertEqual(self.kashmir_dosa.get_all(), "['barley bread', 'mango lasis'] ", "needs to be list of the items")

    def test_update(self):

        """ 080A: Valid Update """

        self.logPoint()

        self.kashmir_dosa.add_menu_item(self.barley_bread)
        self.kashmir_dosa.add_menu_item(self.mango_lasi3)

        mango_lasi = Drink("mango lasi", 8, datetime.date(2017, 9, 12), 6.99, 80, "lasi producer ltd", 129.99, False,
                           False)

        mango_lasi.set_id(2)

        self.kashmir_dosa.update(mango_lasi)

        self.assertEqual(self.kashmir_dosa.get_by_id(2).get_price(), 6.99)


    def test_get_menu_item_stats(self):

        self.logPoint()
        """090A Check the stats of the menu"""

        mango_lasi = Drink("mango lasi", 8, datetime.date(2017, 9, 12), 6.99, 80, "lasi producer ltd", 129.99, False,
                           False)

        self.kashmir_dosa.add_menu_item(self.barley_bread)
        self.kashmir_dosa.add_menu_item(self.mango_lasi3)
        self.kashmir_dosa.add_menu_item(mango_lasi)

        stats = self.kashmir_dosa.get_menu_item_stats()

        self.assertEqual(stats.get_total_num_menu_items(), 3)
        self.assertEqual(stats.get_num_foods(), 1)
        self.assertEqual(stats.get_num_drinks(), 2)
        self.assertEqual(stats.get_avg_price_food(), 12.990000)
        self.assertEqual(stats.get_avg_price_drink(), 9.990000)

    def test_init(self):
        """  tests for parameter validation on the filepath parameter """
        pass

    def test_read_menu_from_file(self):
        """ tests file reading """
        pass

    def test_write_menu_to_file(self):
        """ tests file writing """
        pass

    def tearDown(self):

        self.logPoint()

    def logPoint(self):
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))


if __name__ == '__main__':
    unittest.main()