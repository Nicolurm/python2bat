def calcularNotaAcceso(notaBachillerato, notaFaseGeneral):
    notaAcceso= 0.6*notaBachillerato + 0.4*notaFaseGeneral
    return notaAcceso

def calcularNotaAdmision(notaAccseso, m1, m2, a, b):
    notaAdmision = notaAcceso + m1*a + m2*b
    return notaAdmision

notaBachillerato = float(input("nota bachillerato"))
notaFaseGeneral = float(input("nota fase general"))

notaAcceso = calcularNotaAcceso(notaBachillerato, notaFaseGeneral)
print(f"Tu nota de acceso es {notaAcceso}")
m1 = float(input("notamateriaespecifica1"))
m2 = float(input("notamateriaespecifica2"))
a = float(input("coeficienteponderacionmateria1"))
b = float(input("coeficienteponderacionmateria2"))

notaAdmision = calcularNotaAdmision(notaAcceso, m1, m2, a, b)

print(f"tu nota de admision es {notaAdmision}")