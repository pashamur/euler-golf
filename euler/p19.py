#!/usr/bin/python

import sys

months = [31,28,31,30,31,30,31,31,30,31,30,31]
months_leap = [31,29,31,30,31,30,31,31,30,31,30,31]

def isleap(n):
	if((n%4==0 and n%100!=0) or (n%400 == 0)):
		return 1
	return 0

def main():
	(year, day, i) = (1900, 1, 0)
	while year < 2001:
		print 'year',year,isleap(year)
		if isleap(year):
			for month in months_leap:
				day += month
				if day%7 == 0:
					i+=1
		else:
			for month in months:
				day += month
				if day%7 == 0:
					i+=1
		year+=1
	print i

if __name__ == "__main__":
	main()
