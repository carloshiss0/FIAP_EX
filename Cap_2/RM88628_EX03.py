votos=[0] * 5
print("De segunda a sexta diga o numero de votos de cada dia!")

for x in range(5):
    votos[x] = int(input("{:3d} Dia! - ".format(x+1)))
cont=0
for x in range(1,5):
    if(votos[x]>votos[cont]):
        cont=x
if(cont==0):
    print("com {:2d} votos o dia campeão é Segunda Feira".format(votos[cont]))
elif(cont==1):
    print("com {:2d} votos o dia campeão é Terça Feira".format(votos[cont]))
elif(cont==2):
    print("com {:2d} votos o dia campeão é Quarta Feira".format(votos[cont]))
elif(cont==3):
    print("com {:2d} votos o dia campeão é Quinta Feira".format(votos[cont]))
else:
    print("com {:2d} votos o dia campeão é Sexta Feira".format(votos[cont]))