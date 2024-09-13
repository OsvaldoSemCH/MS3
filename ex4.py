## https://github.com/Andredev-dias/Base-de-algoritmos-em-C-v3/blob/master/busca2bin.c

vet = []

for cont in range(10):
    vet.append(int(input(f"Informe o {cont + 1}º valor: ")))

busca = int(input("Informe um valor a ser procurado: "))

achou = False
baixo = 0
alto = 9

while(baixo <= alto and not achou):
    medio = (baixo + alto) >> 1
    if(busca < vet[medio]):
        alto = medio - 1
    elif(busca > vet[medio]):
        baixo = medio + 1
    else: achou = True

if(achou): print("FOI ENCONTRADO")
else: print("NÃO FOI ENCONTRADO")
