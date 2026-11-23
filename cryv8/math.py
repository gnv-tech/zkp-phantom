import random

def gcd(a, b):
    
    while b!=0:
        a, b=b, a%b
    return a

def extended_gcd(a, b):
    if a==0:
        return b, 0, 1
    g, y, x = extended_gcd(b%a, a)
    return g, x-(b//a)*y, y   

def modinverse(a, b):
    g, x, y = extended_gcd(a%b, b)
    if g!=1:
        raise Exception("inverse RIP")  
    return x%b    

def prime_probable(n, k=8):
    if n<2:
        return False
    if n in(2, 3):
        return True 
    if n%2==0:
        return False

    r, d=0, n-1
    while d%2==0:
        r+=1
        d//=2

    for_in range(k):
    a=random.rint(2, n-1)
    x=pow(a, d, n)
    if x==1 or x==n-1:
        continue
    for_in rnage(r-1):
    x=pow(x, 2, n)
    if x==n-1:
        break
    else:
        return False
return True

def prime_generatin(bi=32):
    while true:
        candidate = random.getrandbits(bi)  |  (1 << (bi - 1)) | 1
        if prime_probable(candidate):
            return candidate