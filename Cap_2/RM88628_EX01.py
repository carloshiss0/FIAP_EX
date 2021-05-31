# Entrada de Dados
peso = float(input("Informe o peso!"))
altura = float(input("Informe a altura!"))
# Calculo do IMC
imc = peso / altura ** 2
if (imc < 16):
    print("Seu IMC é {:.2f} e voce esta na categoria Baixo peso Grau III !".format(imc))
elif (imc < 17):
    print("Seu IMC é {:.2f} e voce esta na categoria Baixo peso Grau II !".format(imc))
elif (imc < 18.50):
    print("Seu IMC é {:.2f} e voce esta na categoria Baixo peso Grau I !".format(imc))
elif (imc < 25):
    print("Seu IMC é {:.2f} e voce esta no Peso Ideal!".format(imc))
elif (imc < 30):
    print("Seu IMC é {:.2f} e voce esta com Sobrepeso!".format(imc))
elif (imc < 35):
    print("Seu IMC é {:.2f} e voce esta com Obesidade Grau I !".format(imc))
elif (imc < 40):
    print("Seu IMC é {:.2f} e voce esta com Obesidade Grau II !".format(imc))
else:
    print("Seu IMC é {:.2f} e voce esta com Obesidade Grau III !".format(imc))
