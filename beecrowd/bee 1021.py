
n = float(input())
print("NOTAS: ")
print("%i nota(s) de R$ 100.00" % (n//100)) # Perceba que nas notas foi usado // porque eo / arredonda para baixo.  
n = n % 100
print("%i nota(s) de R$ 50" % (n//50))
n = n % 50
print("%i nota(s) de R$ 20" % (n//20))
n = n % 20
print("%i nota(s) de R$ 10" % (n//10))
n = n % 10
print("%i nota(s) de R$ 5" % (n//5))
n = n % 5
print("%i nota(s) de R$ 2" % (n//2))
n = n % 2
print("MOEDAS: ")
print("%i moeda(s) de R$ 1.00" % (n//1))
n = n % 1
print("%i moeda(s) de R$ 0.50" % (int(n/0.5)))
n = n % 0.5
print("%i moeda(s) de R$ 0.25" % (int(n/0.25)))
n = n % 0.25
print("%i moeda(s) de R$ 0.10" % (int(n/0.1)))
n = n % 0.1
print("%i moeda(s) de R$ 0.05" % (int(n/0.05)))
n = n % 0.05
print("%i moeda(s) de R$ 0.01" % (int(n/0.01)))


