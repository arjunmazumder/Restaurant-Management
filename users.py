from orders import Order 
# from menu import Menu
from abc import ABC
class Users(ABC):
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

class Customer(Users):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        self.carts = Order()

    def show_menu(self, restaurent):
        restaurent.menu.show_menu()

    def add_to_cart(self, restaurent, item_name, quantity):
        item = restaurent.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print("Sorry !!!!! item quantity exceeded")
            else:
                item.quantity = quantity
                self.carts.add_items(item)
                print("item added")
        else:
            print("Item not found")

    def view_carts_items(self):
        print("\t\t********View Carts********")
        print("\tName\tprice\tQuantity")
        for item,quantity in self.carts.items.items():
            print(f"\t{item.name}\t{item.price}\t{quantity}")
            
        print(f"Total price : {self.carts.total_price()}")
        
    def pay_bill(self):
        print(f"BDT : {self.carts.total_price()} paid successfully!!!!!!!")
        self.carts.clear()


class Employees(Users):
    def __init__(self, name, email, phone, address, age, designation, salary):
        super().__init__(name, email, phone, address)
        self.age = age
        self.designation = designation
        self.salary = salary

class Admin(Users):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
    
    def add_employee(self, restaurent, employee):
        restaurent.add_employee(employee)

    def view_employees(self, restaurent):
        restaurent.view_employees()

    def add_new_item(self, restaurent, item):
        restaurent.menu.add_menu_item(item)

    def view_item(self, restaurent):
        restaurent.menu.show_menu()


    def delete_item(self, restaurent, item_name):
        restaurent.menu.remove_item(item_name)
     