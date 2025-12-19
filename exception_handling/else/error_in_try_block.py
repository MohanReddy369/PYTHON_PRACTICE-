try:
    x = 10/0  #error
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Division successful, result is", x)
