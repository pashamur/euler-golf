#!/usr/bin/python
import os
os.system('perl -ne \'s/\"//g;@e=split(/,/);foreach(@e){print $_.qq(\n);}\' names.txt > NMS.T')
(total, a) = (0, sorted(open("NMS.T","r").readlines()))
for line in a: 
	for c in line.rstrip(): 
		total+=(ord(c)-ord('@'))*(a.index(line)+1)
print total
