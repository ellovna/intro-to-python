# FUNCTIONS

# Difference
# Write a function, which will calculate the difference of these two numbers
#from Tools.scripts import diff

# num_1 = int(input("Enter first number: "))
# num_2 = int(input("Enter second number: "))


#def difference(num_1, num_2):
    #pass
    #
    # diff = 0
    # if num_1 > num_2:
    #     diff = num_1 - num_2
    # else:
    #     diff = num_2 - num_1
    # return diff


#print('the difference between numbers = ', difference(num_1, num_2))

# Division
# Write a function, which will divide these two numbers

# num_1 = int(input("Enter first number: "))
# num_2 = int(input("Enter second number: "))
#
# def division(num_1, num_2):
#     #pass
#     result = 0
#     if num_1 > num_2:
#      result = num_1 / num_2
#     else:
#      result = num_2 / num_1
#     return result
#
# print(division(num_1, num_2))


# Function gets random number. If this number is more than ten, return the difference between 100 and this number,
# otherwise return this number multiplied by 10



#random_number = int(input("Please, enter a random number: "))

#
# def function_1(number):
#
#     result = 0
#     if number > 10:
#         result = 100 - number
#     else:
#         result = number * 10
#     return result
#
#
# print(function_1(random_number))


# Your function temperature_convertor gets the temperature in Fahrenheit, convert it to Celsius and return.
# Formula (32°F − 32) × 5/9 = 0°C

# temperature = int(input("Please, enter your number in Fahrenheit: "))
#
#
# def temperature_convertor(fahrenheit_degree):
#     #pass
#     degree_sign = u'\N{DEGREE SIGN}'
#     return f'{fahrenheit_degree} Fahrenheit is: {round((fahrenheit_degree - 32) * 5/9)}{degree_sign}'
#
#
# print(temperature_convertor(temperature))


# Taxi Fare
# In a particular jurisdiction, taxi fares consist of a base fare of $4.00, plus $0.25 for every 140 meters travelled.
# Write a function that takes the distance travelled (in kilometers) as its only parameter and returns the total fare
# as its only result rounded by 2 digits. Write a program that demonstrates the function.

# km = int(input("Please, enter  a distance in km: "))
# # 1 km = 1000 m
# def taxi_fare(distance):
#     #pass
#     return round(4 + (0.25 * (distance * 0.14)), 2)
#
# print(taxi_fare(km))

# examples of usage:
# taxi_fare(10) #21.86