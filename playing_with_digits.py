n = 46288
p = 3

sum = 0

for idx,num in enumerate(list(str(n)),start=p):
    sum += pow(int(num),idx)

if sum % n == 0:
    print(sum//n)
else:
    print(-1)
