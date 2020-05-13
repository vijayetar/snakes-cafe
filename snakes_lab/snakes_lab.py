from textwrap import dedent

menu_dict = {'Wings', 'Cookies', 'Spring Rolls', 'Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden', 'Ice Cream', 'Cake', 'Pie', 'Coffee', 'Tea', 'Unicorn Tears'}

def welcome_cafe():
  print("*"*38)
  print(dedent(""" 
  **    Welcome to the Snakes Cafe!   **
  **    Please see our menu below.    **
  **
  ** To quit at any time, type "quit" **
  """))
  print("*"*38)
  print("\n")

def show_menu():
  menu= """
Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears
"""
  print(dedent(menu))
  print("\n")


def prompt():
  print('*'*35)
  print(dedent("""
  ** What would you like to order? **
  """))
  print('*'*35)

def order_meal():
  # create the dictionery with the item and the order starting at 0
  value = 0
  items_dict = dict.fromkeys(menu_dict,value)
  # now take the order and then check if it exists in the menu_list
  while True:
    prompt()
    order = input()
    if order == "quit":
      break
    if order in items_dict:
      items_dict[order] += 1   
    print(f"** {items_dict[order]} order of {order} have been added to your meal **")

if __name__ == "__main__":
    welcome_cafe()
    show_menu()
    order_meal()
