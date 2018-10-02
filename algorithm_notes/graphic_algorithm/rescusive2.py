import os

def num(x):
    if len(x) == 0:
        return 0;
    else:
        return 1 + num(x[1:]);


print(num([1,2,3,4,5,6,7,8,9,10]));
