# Decorators

def decorator_function(orginal_function):
    def wrapper_function():
        return orginal_function()
    return wrapper_function

def display():
    print('display function ran')

decorated_display = decorator_function(display)

decorated_display()