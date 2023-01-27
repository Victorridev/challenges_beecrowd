from math import sqrt
A,B,C = list(map(float,input().split())) # map(function, iterable, [iterable 2, iterable 3, ...])
triangulo = float(A) * float(C) * 0.5
circulo = ((float(C)**2)*3.14159)
trapezio =(((float(A) + float(B))/2) * float(C))
quadrado = (float(B) ** 2)
retangulo =  (float(B) * float(A))

print("TRIANGULO: %.3f" % triangulo)
print("CIRCULO: %.3f" % circulo)
print("TRAPEZIO: %.3f" % trapezio)
print("QUADRADO: %.3f" % quadrado)
print("RETANGULO: %.3f" % retangulo)


