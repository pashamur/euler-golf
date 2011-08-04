#!/usr/bin/python
(q, num) = (2, 1125899906842624) 
for i in range(0, 156609):
	q *= num
	q %= 10000000000
print 28433*q*2**6+1
