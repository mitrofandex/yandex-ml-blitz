import sys
import math

n = int(sys.stdin.readline())
for _ in range(n):
    r, d = map(float, sys.stdin.readline().split())
    if r == -1:
        r = 7.94521494
    
    r = (math.exp(r) - 4147) / 3456
    d = math.log(d + 1e-6)
    
    score = 0.64890845 * r  - 0.64049816 * d
    print(score)
