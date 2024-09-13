## https://github.com/Andredev-dias/Base-de-Algoritmos-em-C/blob/master/whilepratica05.c

num_pessoas = 0

alt = float(input("Qual a altura da pessoa? \n"))

while(alt > 0):
    sexo = input("Qual o sexo da pessoa?(M)Homens/(F)Mulheres \n")
    num_pessoas += 1
    if(sexo == 'M'):
        resp = (72.7 * alt) - 58
    else:
        resp = (62.1 * alt) - 44.7
    print(f" Seu peso ideal é de: {resp} quilos \n\n")
    
    alt = float(input("Qual a altura da pessoa? \n"))

print(f" {num_pessoas} participantes. \n\n")