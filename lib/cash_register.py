#!/usr/bin/env python3
import ipdb

class CashRegister:

 

  def __init__(self, discount=0):
    self.discount = discount
    self.items = []
    self.total = 0
    self.last_transaction = 0
    

    


  def add_item(self, item, price, quantity=1):
    self.total += price * quantity
    for i in range(quantity):
      self.items.append(item)
      i += 1
    self.last_transaction = price * quantity
  


  def apply_discount(self):
    percentage = self.discount/100
    if self.discount > 0:
      subtract = self.total * percentage
      self.total -= subtract
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    self.total -= self.last_transaction
    

# ipdb_set_trace()

# walmart = CashRegister()
# walmart.add_item("tomato", 9)
# walmart.items
