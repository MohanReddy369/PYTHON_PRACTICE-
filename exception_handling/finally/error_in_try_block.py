try:
    x = 10 / 0 #error
except:
    print("Cannot divide by zero")
finally:
    print("This will always run")
