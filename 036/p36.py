#!/usr/bin/python
def palin(s):
	return s == s[::-1]

s=0
for i in range(1,1000000):
	if palin(bin(i)[2:]) and palin(str(i)):
		s+=i
print s
