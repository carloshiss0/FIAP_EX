# Entrada de Dados
quantidade = int(input("Informe quantas transações voce efetuou hoje!"))
valort=0
media=0
for i in range(quantidade):
    valort += float(input("Informe o valor da {:.0f}ª transação! R$".format(i+1)))
if quantidade>0 :
    media=valort/quantidade
# Resultado
if quantidade < 2:
    print(
        "O valor total gasto foi de: R${:.2f} em {:.0f} transação, fazendo uma media de R${:.2f} por transação!".format(
            valort, quantidade, media))
else:
    print(
        "O valor total gasto foi de: R${:.2f} em {:.0f} transações, fazendo uma media de R${:.2f} por transação!".format(
            valort, quantidade, media))