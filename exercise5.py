def temperature_in_celsius(temperature):
    temperature = int(temperature)
    temperature =  (temperature - 32) * (5 / 9)

    print("The temperature is {} in degrees celsius.".format(temperature))

print("Enter temperature in Fahrenheit:")
input_temperature = input()

temperature_in_celsius(input_temperature)