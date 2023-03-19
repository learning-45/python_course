class Item:
    def  calculate_total_price(self,x,y):
        return x * y


item1 = Item()
item1.name = "phone"
item1.price = 100 
item1.quantity = 5

total_price = item1.calculate_total_price(item1.price,item1.quantity)
print(total_price)
