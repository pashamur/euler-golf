from decimal import *

def f(x):
    return str(Decimal(1) / Decimal(x))[2:]

getcontext().prec=50
strings = [(x, f(x)) for x in range(2,1000) if len(f(x)) > 10]

longest = 1
for (value,string) in strings:
    n = len(string)/2
    while n > 0:
        
