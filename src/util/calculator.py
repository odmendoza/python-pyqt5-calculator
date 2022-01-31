# Calculator module with add, substract, multiply and divide functions.
# # Only natural numbers.
  
def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    else:
        return a / b    

def is_a_natural_number(a):
    result = True
    try:
        int_a = int(a)
    except ValueError:
        result = False
    return result
