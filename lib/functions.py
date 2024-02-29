#!/usr/bin/env python3
def greet_programmer():
    print("Hello, programmer!")
greet_programmer()    

def greet(name):
    print(f"Hello, {name}!")
greet("Alice")    

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
greet_with_default()
greet_with_default("Bob")    

def add(num1, num2):
    return num1 + num2
result = add(3, 5)
print("Result of addition:", result)

def halve(number):
    return number / 2
halved_value = halve(10)
print("Halved value:", halved_value)



