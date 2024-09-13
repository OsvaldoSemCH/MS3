## https://github.com/Andredev-dias/Base-de-Algoritmos-em-C/blob/master/exercicio9aulapratica.c

cod1 = input("QUAL O CODIGO DO SEU SANDUICHE: \n")
cod2 = input("QUAL O CODIGO DA SUA BEBIDA: \n")

lanche = float(0)
bebida = float(0)

match cod1:
    case 100:
        lanche = 1.20
        print("\nR$ 1.20")
    case 101:
        lanche = 1.30
        print("\nR$ 1.30")
    case 102:
        lanche = 1.50
        print("\nR$ 1.50")
    case 103:
        lanche = 1.70
        print("\nR$ 1.70")
    case _:
        print("COD INCORRETO")

match cod2:
    case 201:
        bebida = 1.20
        print("\nR$ 1.20")
    case 202:
        bebida = 1.50
        print("\nR$ 1.50")
    case 203:
        bebida = 0.70
        print("\nR$ 0.70")
    case _:
        print("COD INCORRETO")
        
pagar = lanche + bebida

print(f"\nTOTAL A PAGAR: {round(pagar, 2)}")