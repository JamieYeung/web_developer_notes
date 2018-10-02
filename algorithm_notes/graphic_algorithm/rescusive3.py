import os

def big(x):
    if len(x) <= 1:
        return x[0];
    else:
        m = big(x[1:])
        if m > x[0]:
            return m
        else:
            return x[0]


print(big([1,2,3,4,100]))
