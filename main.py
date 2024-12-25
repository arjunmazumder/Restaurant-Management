from users import Users,Customer,Employees,Admin
from orders import Order
from restaurent import Restaurent
from food_item import FoodItem
from menu import Menu

mr_restaurent = Restaurent("Ma Baba")

#customer Menu
def Customer_Menu():
    name = input("Enter Your Name : ")
    email = input("Enter Your Email : ")
    phone = input("Enter Your Phone Number : ")
    address = input("Enter Your Current address : ")

    customer = Customer(name=name, email=email, phone=phone,address=address)
    

    while True:
        print(f"\tWellcome {customer.name} !!!!!!!!!!")
        
        print("\t1. View Menu")
        print("\t2. Add item to Cart")
        print("\t3. View Cart Item")
        print("\t4. PayBill")
        print("\t5. Exit")

        choice = int(input("Enter Your Choice : "))
        if choice == 1:
            customer.show_menu(mr_restaurent)
        elif choice == 2:
            item_name = input("Enter the item name : ")
            item_quantity = int(input("Enter the item quantity : "))
            customer.add_to_cart(mr_restaurent,item_name,item_quantity)
        elif choice == 3:
            customer.view_carts_items()
        elif choice == 4:
            customer.pay_bill()
        elif choice == 5:
            break
        else:
            print("Invalid choice!!!")
            print("Please, Enter right choice.")

""" 
    Amin Interface
"""
def admin_Menu():
    name = input("Enter Your Name : ")
    email = input("Enter Your Email : ")
    phone = input("Enter Your Phone Number : ")
    address = input("Enter Your Current address : ")

    admin = Admin(name=name, email=email, phone=phone,address=address)
    

    while True:
        print(f"\tWellcome {admin.name} !!!!!!!!!!")
        
        print("\t1. add_employee")
        print("\t2. view_employees")
        print("\t3. add_new_item")
        print("\t4. view item.")
        print("\t5. delete_item")
        print("\t6. Exit")

        choice = int(input("Enter Your Choice : "))
        if choice == 1:
            name = input("Enter Your name : ")
            email = input("Enter Your email : ")
            phone = input("Enter Your Phone Number : ")
            address = input("Enter Your Address : ")
            age = int(input("Enter Your Age : "))
            designaiton = input("Enter Your Designation : ")
            saraly = input("Enter Your Saraly : ")
            employee = Employees(name=name,email=email,phone=phone,address=address,age=age,designation=designaiton,salary=saraly)
            admin.add_employee(mr_restaurent,employee)
            
        elif choice == 2:
            admin.view_employees(mr_restaurent)
        elif choice == 3:
            name = input("Enter Item Name : ")
            price = int(input("Enter Item Price : "))
            quantity = int(input("Enter Item Quantity : "))
            item = FoodItem(name=name, price=price, quantity=quantity)
            admin.add_new_item(mr_restaurent,item)
            
        elif choice == 4:
            admin.view_item(mr_restaurent)
        elif choice == 5:
            item_name = input("Enter Delete Item Name : ")
            admin.delete_item(mr_restaurent,item_name)
        elif choice == 6:
            break
        else:
            print("Invalid choice!!")
            print("Please, Enter current choice")

while True:
    print("\t********Wellcome*********")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")

    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        Customer_Menu()
    elif choice == 2:
        admin_Menu()
    elif choice == 3:
        break
    else:
        print("Invalide input")
        print("Please, Enter correct input")


