class Tech:
    total_products=0
    discount=0.5

    def __init__(self,name,price,weight,color):
        self.name=name
        self.price=price
        self.weight=weight
        self.color=color
        Tech.total_products+=1
    def get_tech_info(self):
        print(f'name is :{self.name}, price is :{self.price},weight:{self.weight},color:{self.color}')

        


    def apply_discount(self):
        self.price=int(self.price-self.price*self.discount)

    def calculate_shipping_cost(self,rate):
        self.rate=rate
        return self.weight*self.rate
    @classmethod
    def total_number_of_product(cls):
        return cls.total_products
    
product1=Tech('laptop',10000,50,'blue')
product2=Tech('laptop2',100050,55,'sky')        
product3=Tech('laptop3',10000,40,'red')

# print(product1.get_tech_info())
print(Tech.total_number_of_product())       

class Laptop(Tech):
    def __init__(self,name,price,weight,color,ram,cpu,storage):

        super().__init__(name,price,weight,color)

        self.ram=ram
        self.cpu=cpu
        self.storage=storage
    def __str__(self):
        return f"Laptop(ram='{self.ram}',cpu='{self.cpu}',storage='{self.storage}' )"

    def __repr__(self):
        return f"Laptop(ram='{self.ram}',cpu='{self.cpu}',storage='{self.storage}' )"    
  
    def set_double_price(self):
        self.price*=2
    def __str__(self):
        return f" Laptop ( price='{self.price}')"

    def change_space(self,new_ram,new_cpu,new_storage):
        if new_ram>self.ram and new_storage>self.storage:
            self.price+=10000

            #update the instance variables
            self.ram=new_ram
            self.cpu=new_cpu
            self.storage=new_storage

laptop=Laptop('asus',5000,10,'red','32GB','500GB',1000)    
# print(str(laptop))
# print(repr(laptop))
# print(laptop)    

product=Laptop('duel',5000,10,'white','32GB','500GB',1000)
print(product)
product.set_double_price()
print(product)

