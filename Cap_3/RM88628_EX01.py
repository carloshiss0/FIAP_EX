# Entrada de Dados
alimentos = int(input("Informe quantos alimentos voce comeu hoje!"))
calorias=0
for i in range(alimentos):
    calorias += float(input("Informe a quantidade de calorias que o {:.0f}º alimento tem!".format(i+1)))
# Resultado

print("Voce consumiu {:.0f} alimentos hoje, totalizando {:.2f} calorias!".format(alimentos,calorias))

