## https://github.com/Andredev-dias/Base-de-Algoritmos-em-C/blob/master/aulapraticacomandofor05.c

totalsexof21 = 0
totalsexof = 0
totalsexom = 0
totalsexom18 = 0
totalidadef = 0
totalidadem = 0

for cont in range(4):
    idade = input("QUAL A IDADE:\n")
    sexo = input("QUAL O SEXO:\n")

    if(sexo=='F'):
        totalidadef = totalidadef + idade
        if(idade>=21):
            totalsexof21 += 1
        else:
            totalsexof += 1
        
    if(sexo=='M'):
        totalidadem = totalidadem + idade
        if(idade>=18):
            totalsexom18 += 1
        else:
            totalsexom += 1

mediaf = totalidadef/(totalsexof + totalsexof21)
mediam = totalidadem/(totalsexom + totalsexom18)

print(f"Total do sexo feminio e maior que 21 é de: {totalsexof21} \n",)
print(f"Total do sexo masculino e maior que 18 é de: {totalsexom18} \n",)
print(f"Media de idade do sexo feminino é de: {round(mediaf, 2)} \n",)
print(f"Media de idade do sexo masculino é de: {round(mediam, 2)} \n\n\n",)