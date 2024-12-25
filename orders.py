class Order:
    def __init__(self):
        self.items = {}

    def add_items(self, item):
        if item in self.items:
            self.items[item] += item.quantity 
        else:
            self.items[item] = item.quantity

    def remove_cart_item(self, item):
        if item in self.items:
            del self.items[item]
        else:
            print(f"Sorry!!! Not found")    
    

    def total_price(self):
         return sum(item.price * quantity for item, quantity in self.items.items())
    
    def clear(self):
        self.items = {}
