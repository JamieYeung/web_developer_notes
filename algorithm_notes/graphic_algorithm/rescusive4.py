import os

def search(x, a):
    if len(x) <= 1:
        return "find0"
    else:
        m = search(x[1:], a)
        if x[0] == a:
            return "find1"
        else:
            return "find2"
print(search([1,3,4,5], 5))

