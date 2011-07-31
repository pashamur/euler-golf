#!/usr/bin/python

import sys

len_lookup = {}

def recurse(orig, cur, seq_len):
	if cur == 1:
		len_lookup[orig] = seq_len+1
		return seq_len
	if cur in len_lookup:
		len_lookup[orig] = seq_len + len_lookup[cur]
		return seq_len + len_lookup.get(cur)
	if cur%2 == 0:
		return recurse(orig, cur/2, seq_len+1)
	else:
		return recurse(orig, 3*cur+1, seq_len+1)

def main():
	max_val = 0
	max_i = 0
	len_lookup[1] = 1
	for i in range(1, 1000000):
		val = recurse(i, i, 0)
		if val > max_val:
			max_val = val
			max_i = i
		if(i%10000 == 0):
			print i/10000,"% done"
	print max_i, max_val

if __name__ == "__main__":
	main()
