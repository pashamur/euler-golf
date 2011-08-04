#!/usr/bin/python
q = ""
for i in range(1, 250000):
	q+=str(i)
print int(q[1-1])*int(q[10-1])*int(q[100-1])*int(q[1000-1])*int(q[10000-1])*int(q[100000-1])*int(q[1000000-1])
