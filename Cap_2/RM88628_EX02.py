# Entrada de Dados!
plano = str(input("Informe seu Plano!"))
faturamento = float(input("Informe seu Faturamento!"))
bonus = 0
plano = plano.upper()
if (plano == "BASIC"):
    bonus = faturamento * 0.30
elif (plano == "SILVER"):
    bonus = faturamento * 0.20
elif (plano == "GOLD"):
    bonus = faturamento * 0.10
elif (plano == "PLATINUM"):
    bonus = faturamento * 0.05
print("O bonus sobre seu faturamento a ser pago será de: R$ {:.2f} !".format(bonus))
