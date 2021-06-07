#!/usr/bin/env python3

# Created by: Felipe Garcia Affonso
# Created on: June 2021
# This program generate random numbers and uses a 2d array to get the average

import random


def twod_list_average(list_of_numbers):
    # this function get a 2d array average
    average = 0

    for rows_counter in range(0, len(list_of_numbers)):
        for columns_counter in range(0, len(list_of_numbers[0])):
            average += list_of_numbers[rows_counter][columns_counter]

    average = float(average / (len(list_of_numbers) * len(list_of_numbers[0])))

    return average


def main():
    # This function is the main function and generate random numbers
    numbers = []
    try:
        rows = int(input("How many rows do you want? "))
        columns = int(input("How many columns do you want? "))
    except Exception:
        print("\nThis input is invalid, please, insert an integer.")

    print()

    for rows_counter in range(0, rows):
        temp = []
        for columns_counter in range(0, columns):
            random_number = random.randint(0, 50)
            temp.append(random_number)
            print("{:02d} ".format(random_number), end="")
        print()
        numbers.append(temp)

    average = twod_list_average(numbers)

    print("\nThe average is: {}".format(average))

    print("\nDone.")


if __name__ == "__main__":
    main()
