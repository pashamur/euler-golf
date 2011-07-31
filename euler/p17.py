#!/usr/bin/python

import sys

small_num = { 0  :  "zero", 1  :  "one", 2  :  "two", 3  :  "three", 4  :  "four", 
					 5  :  "five", 6  :  "six", 7  :  "seven", 8  :  "eight", 
					 9  :  "nine", 10 :  "ten", 11  :  "eleven", 12: "twelve", 
					 13: "thirteen", 14: "fourteen", 15: "fifteen",	16: "sixteen", 
					 17: "seventeen", 18: "eighteen", 19: "nineteen"}

tens = {2  :  "twenty", 3  :  "thirty", 4  :  "forty", 5  :  "fifty", 
			  6  :  "sixty", 7  :  "seventy", 8  :  "eighty", 9  :  "ninety" }

def sm_getsize(n):
	if n < 20:
		return len(small_num.get(n))
	elif n % 10 == 0:
		return len(tens.get(int(n/10)))
	else:
		return len(tens.get(int(n/10)))+len(small_num.get(n%10))

def getsize(n):
	if n<100:
		return sm_getsize(n)
	elif n%100 == 0:
		return len(small_num.get(n/100)) + len("hundred")
	else:
		return len(small_num.get(n/100)) + len("hundredand") + sm_getsize(n%100) 

def main():
	total = 0
	for i in range(1,1000):
		total += getsize(i) 
	print total+len("onethousand")

if __name__ == "__main__":
	main()
