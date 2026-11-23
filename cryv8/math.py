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
    