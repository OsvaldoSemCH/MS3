## https://github.com/Andredev-dias/Base-de-Algoritmos-em-C_v2/blob/master/listalaco_sexoaltura.c


print("#######################################")
print("\n           ANÁLISE DE FICHAS")
print("\n#######################################")

somaturma = 0
somamulher = 0
maioralt = 0
menoralt = 999
altura = []

for i in range(4):
    
    print("\n ------------------------------------------------------------------");
    genero = int(input(f"\n ({i+1}) - Qual seu gênero (1 - Masculino / 2 - Feminino): "))

    altura.append(int(input(" ({i+1}) - Insira sua altura: ")))

    somaturma = somaturma + altura[i]
    if(genero == 2):
        somamulher += 1

    if(altura[i] > maioralt):
        maioralt = altura[i]

    if(altura[i] < menoralt):
        menoralt = altura[i]

medaltturma = somaturma / 4
mediaaltmulher = somamulher / 4

print("\n ****************************************************")
print("\n               R E S U L T A D O S")
print("\n ****************************************************")
print(f" A média de altura das mulheres é: {mediaaltmulher}")
print(f" A maior altura da turma é: {maioralt}")
print(f" A menor altura da turma é: {menoralt}")
print(f" A média de altura da turma é: {medaltturma}")