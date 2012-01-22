import math

def rot(x):
  x = str(x)
  for i in xrange(len(x)):
    yield int(x)
    x = x[1:]+x[0]

def isPrime(x):
  return all(x%y!=0 for y in xrange(2,int(math.sqrt(x)+1)))

def circPrimes(limit):
  return [n for n in xrange(2, limit) if all(isPrime(d) for d in rot(n))]

print len(circPrimes(1000000))
