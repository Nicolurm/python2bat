def calcularintereses(p,r,t,n)
    A = p*(1+r/n)**(n*t)
    return A
p = float(input("capital inicial"))
r = float(input("interés anual en porcentaje"))
t = float(input("número de año"))
n = float(input("nº de periodo por año"))

capitalfinal = calcularintereses(p,r,t,n)
print(f"la cantidad final despues de {t} de años será {capitalfinal}")