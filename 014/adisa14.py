Col_long=[]
Col_length=[1]

for n in range (1,1000001):
	if(n%10000 == 0):
		print (n/10000),"% done\n"
	seq_n=n
	col_n=1
	while seq_n>1:
		if seq_n%2==0:
			col_n +=1
			seq_n=seq_n/2
		else:
			col_n +=1
			seq_n=3*seq_n+1
	
	Col_length.append(col_n)
	Col_length.sort()
	if col_n==Col_length[-1]:
		Col_long.append(n)

print Col_long[-1]
