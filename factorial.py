# No of trailing zeros in a factorial

n = int(input())

'''
sum = 0
count = 1
while( n//pow(5,count) > 0):
    sum += n//pow(5,count)
    count += 1

print(sum)
'''


def zeros(n):
  x = n//5
  return x+zeros(x) if x else 0

print(zeros(n))
