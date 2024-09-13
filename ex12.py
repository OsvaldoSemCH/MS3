## https://github.com/Andredev-dias/Base-de-Algoritmos-em-C/blob/master/vetmatricula.c

vetmatricula = []
cont = 0
for cont in range(5):
    vetmatricula.append(int(input("DIGITE O NÚMERO PARA CADASTRO DE MATRÍCULA: ")))

busca = int(input("Informe a matrícula para consulta: "))

cont = 0
for cont in range(5):
    if(busca == vetmatricula[cont]):
        break

if(cont == 5):
    print("\n Matricula não encontrada")
else:
    print("Encontrado")
