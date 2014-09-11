__author__ = 'dwight'

# One acre of land is equivalent to 43,560 square feet. Write a program that asks the user to enter the total square
# feet in a tract of land and calculates the number of acres in the tract.

SQUARE_FEET_PER_ACRE = 43560;

square_feet = (int(input('Enter number of square feet in land tract: ')))
acres = square_feet / SQUARE_FEET_PER_ACRE
print('Number of acres:', format(acres, '.2f'))