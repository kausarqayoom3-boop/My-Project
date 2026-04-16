def add(a, b):
   return a + b

def sub(a, b):
   return a - b

def mul(a, b):
   return a * b

def divide(a, b):
   if b == 0:
     raise ValueError("Cannot Divide By Zero")

   return a / b
