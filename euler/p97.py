#!/usr/bin/python

import sys

def main():
	num = 1125899906842624 # == 2**50 
	q=2
	for i in range(0, 156609):
		q *= num
		q %= 10000000000
	print 28433*q*2**6+1

if __name__ == "__main__":
	main()
