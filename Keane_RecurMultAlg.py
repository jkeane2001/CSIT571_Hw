from math import ceil, floor
def recurMult(x,y):

    if (x < y):
        return recurMult(y,x)
    elif y != 0:
        return (x + recurMult(x, ceil(y-1)))
    else:
        return 0

#print(recurMult(5,2))
#print(recurMult(12,12))
#print(recurMult(2048,1024))
#print(recurMult(5678,1234))
