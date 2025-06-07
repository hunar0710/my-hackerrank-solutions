import math

n = int(input().strip())
letters = input().split()
k = int(input().strip())

count_a = letters.count('a')
total = math.comb(n, k)
zero_a = math.comb(n - count_a, k)
prob = 1 - zero_a / total

print(prob)