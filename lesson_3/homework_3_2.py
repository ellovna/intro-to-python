# Enter a number between 1 and 20, save this value to number variable.
# If number is greater than 0 and less than or equal to 7, save the number * 10 to result_1.
# If number is  greater than 7 and less than or equal to 15, save the result of floor division of the number divided by
# 3 to result_1 variable
# If number is  greater than 15 and less than or equal to 20, save the number raised to the power 3 to result_1
# Else save the text "Wrong value" to result_1

# import math
# number = int(input("Enter a number between 1 and 20: "))
# if 0 <= number <= 7:
#     result_1 = number * 10
# elif 7 <= number <= 15:
#     result_1 = math.floor(number / 3)
# elif 15 <= number <= 20:
#     result_1 = "Wrong value"
# else:
#     result_1 = "Please, enter a number between 1 and 20"
# print(result_1)


# Enter two numbers between 1 and 10, save this values to number_1 variable and number_2 variables.
# If number_1 and number_2 are greater than 0 and less than or equal to 5 save in the product of their multiplication
# to result_2
# If one of the variables (number_1 or number_2) is greater than 5 and less than or equal to 10, but the other isn't,
# then save the sum of the two numbers to result_2
# If both numbers are greater than 5 and less than or equal to 10, multiply their sum by 3 and save it to result_2
# Else save the text "Wrong values, try again" to result_28

# number_1 = int(input("Please, enter a number between 1 and 10: "))
# number_2 = int(input("Please, enter the second number between 1 and 10: "))
# if 0 < number_1 <= 5 and 0 < number_2 <= 5:
#     result_2 = number_1 * number_2
# if (5 < number_1 <= 10 and not (5 < number_2 <= 10)) or (5 < number_2 <= 10 and not (5 < number_1 <= 10)):
#     result_2 = number_1 + number_2
# elif 5 < number_1 <= 10 and 5 < number_2 <= 10:
#     result_2 = (number_1 + number_2) * 3
# else:
#     result_2 = "Wrong value try again"
# print(result_2)

# Enter your first name and save it to first_name variable,
# then Enter last name and save it to last_name
# If first_name or last_name are shorter than 6 characters, save a full name (with a space between) to result_3
# Else save first_name to result_3 as many times as length of last_name value

# first_name = input("Please, enter your first name: ")
# last_name = input("Please, enter your last name: ")
# if len(first_name) < 6:
#     result_3 = first_name + " " + last_name
# else:
#     result_3 = len(last_name)
# print(result_3)


# Enter a random number. Save this value to random_number variable
# If this number is less 10 or greater than 99, save the text "Please, put in a number between 10 and 99" to result_4
# If a number doesn't meet the first condition, find the remainder of random_value divided by 2.
# If it is 0, save the text "Even number" to result_4 , else save the message "Odd number"

# random_number = int(input("Enter a random number: "))
# if random_number < 10 or random_number > 99:
#     result_4 = "Please, put in a number between 10 and 99"
# else:
#     result_4 = random_number % 2
#     if result_4 == 0:
#         result_4 = "Even number"
#     else:
#         result_4 = "Odd number"
# print(result_4)
