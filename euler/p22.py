#!/usr/bin/python
import sys
import os
os.system('perl -ne \'s/\"//g;@e=split(/,/);foreach(@e){print $_.qq(\n);}\' names.txt > NMS.T')
def compute(l):
	tot=0
	for c in l.rstrip(): tot+=(ord(c)-ord('A')+1)
	return tot
(total, i) = (0, 1)
for line in sorted(open("NMS.T","r").readlines()): 
	total += i*compute(line)
	i=i+1
print total
