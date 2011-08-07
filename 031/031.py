#!/usr/bin/python
variants = 0
coins = [200, 100, 50, 20, 10, 5, 2, 1]

def count(n, last_coin):
  if n == 0:
    return 1
  sum = 0
  for i in range(0,8):
    if n >= coins[i] and coins[i] <= last_coin:
      sum += count(n-coins[i], coins[i])
  return sum

print count(200,400)
