n = int(input())


def perimeter(n):
    a,b = 1,2
    while n:
        a,b,n = b,a+b,n-1


'''
a = 1
b = 1
i,c,s=0,0,0
while(i < n-1):
    c = a+b
    a,b = b,c
    s = s+c
    i += 1
'''

def perimeter(n):
    a, b = 1, 2
    while n:
        a, b, n = b, a + b, n - 1

    return 4 * (b - 1)

print(perimeter(n))
