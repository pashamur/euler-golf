import math

def isPrime(x):
    if x % 2 == 0 and x != 2 or x <= 1: return False
    for i in range(3, int(math.sqrt(x))+1, 2):
        if x%i == 0: return False
    return True

def eval(a,b,n):
    return n*n + a*n + b;

def testLength(a, b):
    n = 0
    while isPrime(eval(a,b,n)):
        n += 1
    return n

def maxValues():
    (max_a,max_b,max_len) = (0,0,0)
    for a in range(-999, 1000):
        for b in range(-999, 1000):
            if testLength(a,b) > max_len:
                (max_a, max_b, max_len)=(a,b,testLength(a,b))
        if (a+1000) % 100 == 0:
            print str((a + 1000)/20)+'%'
    return (max_a, max_b)

def solve():
    return reduce(lambda x,y: x*y, maxValues())
