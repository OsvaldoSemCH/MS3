## https://github.com/Andredev-dias/Base-de-Algoritmos-em-C_v2/blob/master/listacondicional6.c


id = input("Qual sua matricula?\n")
nota1 = input("Informe dua 1ª nota:\n")
nota2 = input("Informe dua 2ª nota:\n")
nota3 = input("Informe dua 3ª nota:\n")

media = (nota1 + nota2 + nota3) / 3

print(f"Média: {round(media, 2)}")

if(media >= 9):
    print("Conceito: A, APROVADO.")
elif(media >= 7.5):
    print("Conceito: B, APROVADO.")
elif(media >= 6):
    print("Conceito: C, APROVADO.")
elif(media >= 4):
    print("Conceito: D, REPROVADO.")
else:
    print("Conceito: E, BURRO.")
    