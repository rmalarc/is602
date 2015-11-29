#!/usr/bin/python

# Author: Mauricio Alarcon <rmalarc@msn.com>

#1. fill in this function
#   it takes a list for input and return a sorted version
#   do this with a loop, don't use the built in list functions
def sortwithloops(input):
    sorted_input = input[:]
    is_sorted = False
    while not is_sorted:
        changes = False
        for i in range(len(sorted_input)-1):
            if (sorted_input[i] > sorted_input[i+1]):
                changes = True
                tmp = sorted_input[i]
                sorted_input[i] = sorted_input[i+1]
                sorted_input[i+1] = tmp
        is_sorted = not(changes)
    return sorted_input

#2. fill in this function
#   it takes a list for input and return a sorted version
#   do this with the built in list functions, don't us a loop
def sortwithoutloops(input):
    sorted_input = input[:]
    sorted_input.sort()
    return sorted_input#return a value

#3. fill in this function
#   it takes a list for input and a value to search for
#	it returns true if the value is in the list, otherwise false
#   do this with a loop, don't use the built in list functions
def searchwithloops(input, value):
    found=False
    for i in range(len(input)):
        found = input[i] == value
        if (found):
            break
    return found #return a value

#4. fill in this function
#   it takes a list for input and a value to search for
#	it returns true if the value is in the list, otherwise false
#   do this with the built in list functions, don't use a loop
def searchwithoutloops(input, value):
    return value in input #return a value

if __name__ == "__main__":
    L = [6,3,6,3,13,5,5]
    print sortwithloops(L) # [3, 3, 5, 5, 6, 6, 13]
    print sortwithoutloops(L) # [3, 3, 5, 5, 6, 6, 13]
    print searchwithloops(L, 5) #true
    print searchwithloops(L, 11) #false
    print searchwithoutloops(L, 5) #true
    print searchwithoutloops(L, 11) #false
