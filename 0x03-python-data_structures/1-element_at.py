#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return(none)
    length = len(my_list)
    if idx > length - 1:
        return(none)
    return(my_list[idx])
