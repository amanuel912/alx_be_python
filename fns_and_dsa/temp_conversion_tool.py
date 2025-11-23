FARENHEIT_TO_CELSIUS_FACTOR = 5.0 / 9.0
CELSIUS_TO_FARENHEIT_FACTOR = 9.0 / 5.0

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FARENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FARENHEIT_FACTOR) + 32

def main():
    temprature = input("Enter the temperature to convert: ")
    if temprature is not float and not temprature.isdigit():
        print("Please enter a valid number for temperature.")
    temp_unit = input("is this temperature in Celsius or Fahrenheit? (C/F): ")
    if temp_unit == 'C':
        converted_temp = convert_to_fahrenheit(float(temprature))
        print(f"{temprature}°C is {converted_temp}°F")
    else:
        converted_temp = convert_to_celsius(float(temprature))
        print(f"{temprature}°F is {converted_temp}°C")