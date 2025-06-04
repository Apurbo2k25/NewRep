def celsius_to_fahrenheit(c):
    f = (9/5) * c + 32
    print(f"Your {c} Celsius = {f} Fahrenheit")
    return f

def fahrenheit_to_celsius(f):
    c = (5/9) * (f - 32)
    print(f"Your {f} Fahrenheit = {c} Celsius")
    return c

check = input("Enter 1 for Celsius to Fahrenheit and 2 for Fahrenheit to Celsius conversion: ")

if check == '1':
    celsius_value = float(input("Enter temperature in Celsius: "))
    celsius_to_fahrenheit(celsius_value)

elif check == '2':
    fahrenheit_value = float(input("Enter temperature in Fahrenheit: "))
    fahrenheit_to_celsius(fahrenheit_value)

else:
    print("Error 404! You chose a wrong number!")
    exit()