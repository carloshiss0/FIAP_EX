# Entrada de Dados
valor = int(input("Informe um valor inteiro!"))
# Calculos
anterior = 0
proximo = 0
veri=0
while(proximo <= valor and veri==0):
    if(proximo==valor):
        veri=1
    proximo = proximo + anterior
    anterior = proximo - anterior
    if(proximo == 0):
        proximo = proximo + 1

# Resultado
if veri==1:
    print(
        "A Ação Bem sucedida!")
else:
    print(
        "A Ação Falhou...")



