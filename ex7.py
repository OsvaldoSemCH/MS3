## https://github.com/Andredev-dias/Base-de-Algoritmos-em-C_v2/blob/master/revisao1.c

codtime = input("Qual o Código do seu Time:\n")
numtimes = 0
media = 0

while(codtime > 0):
    idadesoma = 0
    for cont in range(3):
        
        nome = input("Qual seu Nome:\n")
    
        idade = input("Qual sua idade:\n")
    
        print(f"Obrigado pelo cadastro {nome}\n")
        idadesoma = idadesoma + idade
    numtimes += 1
    media = idadesoma / 3
    
    print(f"A media de idade deste time é de {round(media, 2)} anos.")
    print(f"%{numtimes}º time calculado.\n")
    
    codtime = input("Qual o Código do seu Time:\n")