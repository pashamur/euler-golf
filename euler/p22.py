#!/usr/bin/python
import os
os.system('perl -ne \'s/\"//g;@e=split(/,/);foreach(@e){print $_.qq(\n);}\' names.txt > NMS.T')
(total, i) = (0, 1)
for line in sorted(open("NMS.T","r").readlines()): 
	for c in line.rstrip():
		total+=(ord(c)-ord('A')+1)*i
	i=i+1
print total
