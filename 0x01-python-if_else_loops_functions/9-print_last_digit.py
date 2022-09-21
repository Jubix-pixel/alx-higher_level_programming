#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        lst_digit = number % 10
    else:
        lst_digit = number % -10
        lst_digit *= -1
    print("{:d}".format(lst_digit), end='')
    return (lst_digit)
