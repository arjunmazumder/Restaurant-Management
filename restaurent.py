from menu import Menu
class Restaurent:
    def __init__(self, name):
        self.name = name
        self.employees=[]
        self.menu = Menu()

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"{employee.name} is added successful!!")

    def view_employees(self):
        print(f"\tEmployees List !!!!!!!")
        print(f"\tName\tEmail\t\tPhone\tAddress\tage\tdesignation\tsalary")

        for employee in self.employees:
            print(f"\t{employee.name}\t {employee.email}\t {employee.phone}\t {employee.address}\t {employee.age}\t {employee.designation}\t {employee.salary}")    
