#temperatures between Celsius and Fahrenheit

# function for converting the temperature 
def converter(temperature, unit):
    
    if unit=="Celsius":
        print("Temperature in Fahrenheit is : " , (temperature * 9/5) + 32, "Fahrenheit ")
    else :
       print("Temperature in Celsius is:", (temperature - 32) * 5 / 9,"Celsius")

# utilizing the function 
temperature = 25
unit = "Celsius"

converter(temperature,unit)