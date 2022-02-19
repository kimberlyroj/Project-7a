# Author: Kimberly Rojas
# GitHub username: kimberlyroj
# Date: 2/18/2022
# Description: A function named square_list that takes as a parameter a list of numbers and replaces each value with the square of that value
def square_list(lst):
    for i in range(len(lst)):
        lst[i] = lst[i] * lst[i]