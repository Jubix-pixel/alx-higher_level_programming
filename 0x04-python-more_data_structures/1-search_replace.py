#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for i in range(len(my_list)):
        n = search
        x = replace
        if my_list[i] == n:
            my_list[i] = x
