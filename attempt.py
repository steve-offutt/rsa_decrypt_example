import sys
'''
Problem:
p, q < 10000
e = 1441, N = 30648649

C = [16853416, 16843366, 11200857, 
     3457888, 4543, 14067518, 
     23448235, 3061504, 7348356, 
     3061504, 27797407, 6854145, 7348356, 
     19224935, 27797407, 3061504,
     27797407, 21730072, 15304063, 
     3061504, 21704130, 22828108, 
     27797407, 21730072, 24345473]
Find two numbers e and d that are relatively prime to N and for which e*d = 1
mod r:

$factor 30648649
30648649: 4729 6481
'''


# borrowed functions from
# https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm#Iterative_algorithm_3
# Extended Euclidean algorithm
def xgcd(b, n):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  b, x0, y0

# x = mulinv(b) mod n, (x * b) % n == 1
def mulinv(b, n):
    g, x, _ = xgcd(b, n)
    if g == 1:
        return x % n

N = 30648649
p = 4729
q = 6481
e = 1441
r = (p-1)*(q-1)
d = mulinv(e,r)

# Ciphertext
C = [16853416, 16843366, 11200857, 
     3457888, 4543, 14067518, 
     23448235, 3061504, 7348356, 
     3061504, 27797407, 6854145, 7348356, 
     19224935, 27797407, 3061504,
     27797407, 21730072, 15304063, 
     3061504, 21704130, 22828108, 
     27797407, 21730072, 24345473]

check = d*e % r
print 'd: {0}, e: {1}, r: {3}, d*e mod(r): {2}'.format(d, e, check, r)

for c in C:
    sys.stdout.write("%s" % chr(c**d%N))
    sys.stdout.flush()
print
