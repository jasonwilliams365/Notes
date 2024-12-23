def greet (name):
    return f"Hello, {name}!"
print(greet("Jason"))



def add_numbers (a, b=0):
    return a + b
print(add_numbers(5))
print(add_numbers(5, 10))