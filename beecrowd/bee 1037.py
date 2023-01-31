Q = input()

if 0<=float(Q)<=25 :
    print('Intervalo [0,25]')
elif 25<=float(Q)<=50:
    print('Intervalo (25,50]')
elif 50<=float(Q)<=75:
    print('Intervalo (50,75]')
elif 75<=float(Q)<=100:
    print('Intervalo (75,100]')
else:
    print("Fora de intervalo")