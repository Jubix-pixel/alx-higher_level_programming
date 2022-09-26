#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return(none)
    length = len(my_list) - 1
    if idx > length:
        return(none)
    return(my_list[idx])
