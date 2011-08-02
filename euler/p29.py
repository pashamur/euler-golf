#!/usr/bin/python

import math

def main():
	l = []
	for i in range(2,101):
		for j in range(2,101):
			c = i**j
			if c not in l:
				l.append(c)
	print len(l) 

if __name__ == "__main__":
	main()
