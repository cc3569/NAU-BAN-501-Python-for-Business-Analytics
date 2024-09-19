# -*- coding: utf-8 -*-
"""[BAN 501] Module 3 Project Assignment

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SRMv2mNIo4RAjcWsNrg8QzKeiszHqmOq

**Module 3 Project Assignment - Inventory Management Using Object-Oriented Programming (OOP)**

Cole T. Catron

NAU - The W.A. Franke College of Business

Dr. Martin Hassell

September 18, 2024
"""

# "Product" class with attributes "name", "price", and "quantity"
class Product:
  def __init__(self, name, price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity

# A method to increase the quantity of the product by a specified amount
  def add_stock(self, amount):
    self.quantity += amount

# A method to decrease the quantity of the product by a specified amount
  def sell(self, amount):
    self.quantity -= amount

# A method to get the total value of the product
  def get_value(self):
    return self.price * self.quantity

# Shows product names
  def __str__(self):
    return f"Product Name: {self.name}\nPrice: ${self.price:.2f}\nQuantity In Stock: {self.quantity}"

# Product attributes were obtained from target.com
tropicana_orange_juice = Product("Tropicana Pure Premium No Pulp Calcium + Vitamin D Orange Juice - 89 fl oz", 6.99, 20)
tropicana_pineapple_mango = Product("Tropicana Pineapple Mango - 46oz", 2.69, 25)
tropicana_strawberry_limeade = Product("Tropicana Strawberry Limeade - 46oz", 2.69, 30)

# Takes all products and places them in a list
product_list = [tropicana_orange_juice, tropicana_pineapple_mango, tropicana_strawberry_limeade]

# Presents current invenstory
print("========== CURRENT INVENTORY ==========")
for product in product_list:
  print(product)
  print(f"Total Value of Product In Stock: ${product.get_value():.2f}\n")

# Simulates restocking for all products in product list
for product in product_list:
  product.add_stock(10)

# Simulates purchasing of all products in product list
for product in product_list:
  product.sell(2)

# Presents updated inventory
print("========== UPDATED INVENTORY ==========")
for product in product_list:
  print(product)
  print(f"Total Value of Product In Stock: ${product.get_value():.2f}\n")

