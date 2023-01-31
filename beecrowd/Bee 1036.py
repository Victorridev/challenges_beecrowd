import math

def bhaskarax1(A, B ,C):
    if A == 0 :
        print("Not is Second equation")
        return 
    delta = math.pow(B, 2) - 4*A*C
    if delta < 0:
        print("Impossível Calcular")
    elif math.sqrt(delta) < 0:
        print("Impossível Calcular")
    else:
        x1 = (-B + math.sqrt(delta)) / (2*A)
        return x1
def bhaskarax2(A, B ,C):
    if A == 0 :
        print("Not is Second equation")
        return None
    delta = math.pow(B, 2) - 4*A*C
    if delta < 0:
        print("Impossível Calcular")
        return None
    elif math.sqrt(delta) < 0:
        print("Impossível Calcular")
        return None
    else:
        x2 = (-B - math.sqrt(delta)) / (2*A)
        return x2

A, B, C = input().split()
x1 = bhaskarax1(float(A), float(B), float(C))
x2 = bhaskarax2(float(A), float(B), float(C))

print("R1 = %.5f" % x1)
print("R2 = %.5f" % x2)
