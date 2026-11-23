
def divide(a, b):
    x = pow(b, a-1)
    return x%a

print(divide(65537, 273246787654))