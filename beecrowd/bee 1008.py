numero_func = int(input())
numero_hr = int(input())
valor_hr = float(input())

def calcular_horas():
    global numero_hr
    global valor_hr
    
    return float(numero_hr * valor_hr)

print("NUMBER = %i" % numero_func)
print("SALARY = U$ %.2f" %calcular_horas())