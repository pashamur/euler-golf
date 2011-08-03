import math
tot = 0
factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

for i in range(3,2000000):
	str_i = str(i)
	tsum = 0
	for char in str_i:
		tsum += factorials[ord(char)-ord('0')]
	if(tsum == i):
		tot += i
print tot
