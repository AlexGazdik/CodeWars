
'''Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.'''


def find_it(seq):
    dict={}
    for i in seq:
        if i not in dict:
            dict[i]=1
        else:
            dict[i] += 1
    for k,v in dict.items():
        if v % 2==0:
            pass
        else:
            return k
