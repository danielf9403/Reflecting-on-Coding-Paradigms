class Podracer:
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

 
  def repair(self):
    self.condition = "repaired"
    

class AnakinsPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price):
  
  def boost(self):
    self.max_speed *= 2
    

class SebulbasPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price):
  
  def flame_jet(self,other):
    other.condition = "trashed"
    
"""
How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
The central pillar of OOPs - data Abstraction, Encapsulation, Inheritance, and Polymorphism, makes it smooth for programmers to solve complex situations.

Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
no because it would be hard to implement a solution

How in particular did Object Oriented Programming assist in the solving of this problem?
i'm not sure im try to understand it
      
"""