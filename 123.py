import math
n = 10000
res = (n ** 2) / (n * math.log(n, 2))
print(res)

def p(n):
    if n == 0:
        return
    else:
        p(n-1)
        print(n)
p(5)