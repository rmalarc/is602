
import timeit

# Author: Mauricio Alarcon <rmalarc@msn.com>


setup = '''
import numpy
import random

def sortwithloops(input):
    sorted_input = input
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

def sortwithoutloops(input):
    input.sort()
    return input

def sortwithnumpy(input):
    return numpy.sort(numpy.array(input))

def searchwithloops(input, value):
    found=False
    for i in range(len(input)):
        found = input[i] == value
        if (found):
            break
    return found #return a value

def searchwithoutloops(input, value):
    return value in input #return a value

def searchwithnumpy(input,value):
    return True in (numpy.array(L)==value)

random.seed(100)
L = random.sample(range(1, 10000), 100)

'''

if __name__ == "__main__":
    n = 1000

    t = timeit.Timer("t=L[:];sortwithloops(t)",setup=setup)
    print 'sortwithloops: ',t.timeit(n)

    t = timeit.Timer("t=L[:];sortwithoutloops(t)",setup=setup)
    print 'sortwithoutloops: ',t.timeit(n)

    t = timeit.Timer("t=L[:];sortwithnumpy(t)",setup=setup)
    print 'sortwithnumpy: ',t.timeit(n)

    t = timeit.Timer("t=L[:];searchwithloops(t, 4549)",setup=setup)
    print 'searchwithloops: ',t.timeit(n)

    t = timeit.Timer("t=L[:];searchwithoutloops(t, 4549)",setup=setup)
    print 'searchwithoutloops: ',t.timeit(n)

    t = timeit.Timer("t=L[:];searchwithnumpy(L, 4549)",setup=setup)
    print 'searchwithnumpy: ',t.timeit(n)

