idade = int(input())
a = idade/365
rA = idade % 365
rM = rA % 30
m = rA / 30
d = rM % 30
print("{} ano(s)".format(int(a)))
print("{} mes(es)".format(int(m)))
print("{} dia(s)".format(int(d)))