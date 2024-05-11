def convert_to_fahrenheit(celsius):
    return (celsius * 1.8) + 32

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) / 1.8

print("Enter Temperature:")
num = eval(input())
conversion_type = input("Enter 'C' for Celsius to Fahrenheit conversion, 'F' for Fahrenheit to Celsius conversion: ")

result = None

if conversion_type == 'C':
    result = convert_to_fahrenheit(num)
    print(str(num) + " degree Celsius is equal to " + str(result) + " degree Fahrenheit")
elif conversion_type == 'F':
    result = convert_to_celsius(num)
    print(str(num) + " degree Fahrenheit is equal to " + str(result) + " degree Celsius")
else:
    print("Invalid conversion type.")