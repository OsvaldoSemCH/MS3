## https://github.com/Andredev-dias/Base-de-Algoritmos-em-C/blob/master/whilepratica06.c

conttotal = 0
contIA = 0
contIB = 0
contJA = 0
contJB = 0
contADUL = 0

idade = int(input("Qual a idade do nadador?\n"))

while(idade > 0):
    if(idade >= 18):
        conttotal += 1
        contADUL += 1
        print("ADULTO")
    elif(idade >= 14):
        conttotal += 1
        contJB += 1
        print("Juvenil B")
    elif(idade >= 11):
        conttotal += 1
        contJA += 1
        print("Juvenil A")
    elif(idade >= 8):
        conttotal += 1
        contIB += 1
        print("Infantil B")
    elif(idade >= 5):
        conttotal += 1
        contIA += 1
        print("Infantil A")
    idade = int(input("Qual a idade do nadador?\n"))

print(f" Categoria infantil A sao: {contIA}")
print(f" Categoria infantil B sao: {contIB}")
print(f" Categoria juvenil A sao: {contJA}")
print(f" Categoria juvenil B sao: {contJB}")
print(f" Categoria Adultos sao: {contADUL}")
print(f" Total: {conttotal}")