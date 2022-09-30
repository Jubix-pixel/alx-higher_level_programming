#!/usr/bin/python3
def best_score(a_dictionary):
    max_score = max(a_dictionary, key =  a_dictionary.get)
    if max_score == None:
        return (None)
    else:
        return (max_score)
    return (max_score)
