#!/usr/bin/python

import sys

def main():
	(f_prev, f_cur, i) = (1,1,2)
	while len(str(f_cur)) < 1000:
		(f_cur,f_prev)=(f_cur+f_prev,f_cur)
		i=i+1
	print i

if __name__ == "__main__":
	main()
