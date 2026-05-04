# Override the constructor using single level inheritance having product name, product type as a argument of first conctructor and color as argument of derived class
# class product_info1:
#     def __init__(self,name,type):
#         self.name=name
#         self.type=type
#         print("Product name :",self.name)
#         print("Product type :",self.type)

# class product_info2(product_info1):
#     def __init__(self, name, type,color):
#         self.color=color
#         super().__init__(name, type)
#         print("Product color :",self.color)

# data=product_info2("Book","History","Red")

'''Implement following program using single level inheritance 
take product class with product id, product name, product quantity, product price
take product data to input product details by considering req. validations
take product info method to display req details of product 
inherit product class with product detail class and call methods from parent class 
'''

# class product:
#     def input(self):
#         self.id=input("Enter product id :")
#         self.name=input("Enter product name :")
#         self.qty=input("Entr quantity :")
#         self.price=input("Enter product price :")

# class product_detail(product):
#     def display(self):
#         print("Product id :",self.id)
#         print("Product name :",self.name)
#         print("Product quantity :",self.qty)
#         print("Product price :",self.price)
# obj=product_detail()
# obj.input()
# print("\t\t")
# print("Product details are :")
# obj.display()

##-------------------------------------
# class product:
#     def input(self):
#         self.id=input("Enter product id :")
#         self.name=input("Enter product name :")
#         self.qty=input("Entr quantity :")
#         self.price=input("Enter product price :")

# class product_detail(product):
#     def display(self):
#         print("Product id :",self.id)
#         print("Product name :",self.name)
#         print("Product quantity :",self.qty)
#         print("Product price :",self.price)

# data=[]
# num=int(input("How many product details required :"))
# for i in range(num):
#     print(f"Enter Product {i+1} details ")
#     obj=product_detail()
#     obj.input()
#     data.append(obj)

# print("Product details are :")
# for j in data:
#     print("\t\t")
#     j.display()