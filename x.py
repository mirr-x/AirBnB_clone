class MyClass:
    pass


class AnotherClass:
    pass


# Example class name provided as an argument
arg = "MyCass"

arg2 = MyClass()
# Using globals()[arg] to dynamically access the class
my_instance = globals()[arg]()

# Now my_instance is an instance of the MyClass class
print(isinstance(my_instance, MyClass))  # Output: True
