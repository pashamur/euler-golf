#!/usr/bin/python

import sys

def main():
	tot=0
	for i in range(2,1000000):
		dgsum = 0
		for c in str(i):
			dgsum += (ord(c)-ord('0'))**5
		if dgsum == i:
			tot += i
	print tot

if __name__ == "__main__":
	main()
