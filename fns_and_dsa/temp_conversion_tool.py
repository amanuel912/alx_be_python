FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    temprature = input("Enter the temperature to convert: ")
    if not temprature.replace('.', '', 1).isdigit():
        print("Invalid temperature. Please enter a numeric value.")
        return

    temp_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    if temp_unit == 'C':
        converted_temp = convert_to_fahrenheit(float(temprature))
        print(f"{temprature}°C is {converted_temp}°F")
    else:
        converted_temp = convert_to_celsius(float(temprature))
        print(f"{temprature}°F is {converted_temp}°C")

main()
