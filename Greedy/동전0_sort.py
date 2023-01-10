import sys

def input():
  return sys.stdin.readline().rstrip()

N, K = map(int, input().split())

coin_list = []

for i in range(N):
  coin = int(input())
  coin_list.append(coin)

coin_list.sort(reverse=True)
coin_sum = 0

for coin in coin_list:
  coin_sum += K // coin
  K = K % coin

print(coin_sum)