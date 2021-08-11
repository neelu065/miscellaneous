# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


class Vehicle:
    def __init__(self, name, mileage, brand, origin, cost):
        self.mileage = mileage
        self.name = name
        self.brand = brand
        self.origin = origin
        self.cost = cost
        
    def performance(self):
        if self.name == "Tesla":
            print(f"{self.name} performance is excellent")
        elif self.name == "Honda":
            print(f"{self.name} performance need improvement")
            
    def price(self):
        print(f"I hate you")
        if self.cost == 5000:
            print(f"{self.name} is expensive")
        else:
            print(f"{self.name} is affordable")
            
    
result1 = Vehicle("Honda", 15, "Green", "Norway", 6000)
result1.performance()
result1.price()
