import math
import numpy as np

def slowFib(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return slowFib(n - 1) + slowFib(n - 2)

def fib(n):
    
    if n == 0: return 0
    
    cur = 1
    prev = 0
    for i in range(2,n+1):
        temp = cur
        cur = prev + cur
        prev = temp
        
    return cur

def wrongFib(n): #inaccurate version because of floats
    phi = (1 + math.sqrt(5)) / 2
    psi = 1 - phi
    ans = (phi ** n - psi ** n) / math.sqrt(5)
    return round(ans)

def fastFib(n):
    F = np.array([[1, 1], [1, 0]])
    inp = np.array([[1], [0]])
    ans = np.linalg.matrix_power(F, n)
    return ans[1][0]
    
for i in range(0,90):
    fast = fastFib(i)
    slow = fib(i)
    print("Fast: %d Slow: %d Error: %d" %(fast, slow, fast-slow))
