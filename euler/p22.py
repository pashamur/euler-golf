#!/usr/bin/python
import sys
import os
os.system('perl -ne \'s/\"//g;@e=split(/,/);foreach(@e){print $_.qq(\n);}\' names.txt > NMS.T')
def compute(l, tot):
	for c in l.rstrip(): tot+=(ord(c)-ord('A')+1)
	return tot
def main():
	(total, i) = (0, 1)
	for line in sorted(open("NMS.T","r").readlines()): 
		total += compute(line,0)
		i=i+1
	print total
if __name__ == "__main__": main()
