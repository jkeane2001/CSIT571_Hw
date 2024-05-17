#Jack Keane
#CST571_01 Computer Algortithms and Analysis
#PG1 Karatsuba's Algorithm
#27 January 2023
from math import ceil, floor

def karatsuba(x, y):

    if(x < 10 or y < 10):
        return x * y #Performs normal multiplication if x or y is less than 10

    #Calculates the size of x and y
    n = max(len(str(x)), len(str(y)))
    m = floor(n/2)

    #Splits the sequence of the x input in the middle.
    high1 = floor(x / 10**m)
    low1 = x % (10**m)

    #Splits the sequence of the y input in the middle.
    high2 = floor(y / 10**m)
    low2 = y % (10**m)

    #Performs the 3 recursive calls made to the numbers which is about half the size
    z0 = karatsuba(low1, low2)
    z1 = karatsuba(low1 + high1, low2 + high2)
    z2 = karatsuba(high1, high2)

    #Brings each piece back together to form the product
    return int(z2 * (10**(m * 2)) + ((z1-z2-z0) * (10**m))+z0)

print("Testing Karatsuba's algorithm with a couple inputs of various sizes:")
print(karatsuba(2, 5))
print(karatsuba(5678, 1234)) #Ex. from class
print(karatsuba(574534935, 283884342))
print(karatsuba(234241, 897))
print("\n")

print("Product of the two 64 digit numbers:")
print(karatsuba(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627))
#The result of multiplying the two 64 digit integers is
#8539734222673566957498846900491595793628487889746454950813687461572372213054499114931277629325900131223124341791952806582723184

print("\n")
print("Inputs with a power of 2:")
print(karatsuba(256, 128))
print(karatsuba(1024, 2048))
print(karatsuba(32768, 65536))
#I would assume that if the input number is a power of 2 which mean the input numbers are rising exponentially.
#If this is the case then the complexity would increase as the algorithm needs to process number increasing in size.
#Which would mean it would take longer to find the product of these large numbers.