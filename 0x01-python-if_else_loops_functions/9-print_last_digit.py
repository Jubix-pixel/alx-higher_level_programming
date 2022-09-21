#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        lst_digit = number % 10
    else:
        lst_digit = number % -10
        lst_digit = lst_digit * -1
    print("{:d}".format(number), end='')
    return (lst_digit)
