#!/usr/bin/env python3

class CashRegister:

  total = 0
  def __init__(self, discount=0):
    self.discount = discount


  def add_item(self, title, price, quantity=1):
    self.total += price * quantity
    self.title = title

  def apply_discount(self):
    percentage = self.discount/100
    if self.discount > 0:
      subtract = self.total * percentage
      self.total -= subtract
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")
    


