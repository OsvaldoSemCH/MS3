## https://github.com/Andredev-dias/Base-de-Algoritmos-em-C/blob/master/trabalho_condicional.c

i = int(input("Informe o valor de i :\n"))

a = float(input("Informe o valor de a :\n"))

b = float(input("Informe o valor de b :\n"))

c = float(input("Informe o valor de c :\n"))

if (i == 1):
    #ordem crescente
    if (a < b and a < c and b < c):
        print(f"a vale {a} ")
        print(f"b vale {b} ")
        print(f"c vale {c} \n")
    elif (a < b and a < c and c < b):
        print(f"a vale {a} ")
        print(f"c vale {c} ")
        print(f"b vale {b} \n")
    elif (b < a and b < c and a < c):
        print(f"b vale {b} ")
        print(f"a vale {a} ")
        print(f"c vale {c} \n")
    elif (b < a and b < c and c < a):
        print(f"b vale {b} ")
        print(f"c vale {c} ")
        print(f"a vale {a} \n")
    elif (c < a and c < b and a < b):
        print(f"c vale {c} ")
        print(f"a vale {a} ")
        print(f"b vale {b} \n")
    elif (c < a and c < b and b < a):
        print(f"c vale {c} ")
        print(f"b vale {b} ")
        print(f"a vale {a} \n")	
elif(i == 2):
    #ordem decrescente
    if (a > b and a > c and b > c):
        print(f"a vale {a} ")
        print(f"b vale {b} ")
        print(f"c vale {c} \n")
    elif (a > b and a > c and c > b):
        print(f"a vale {a} ")
        print(f"c vale {c} ")
        print(f"d vale {b} \n")

    elif (b > a and b > c and a >c):
        print(f"b vale {b} ")
        print(f"a vale {a} ")
        print(f"c vale {c} \n")
    elif (b > a and b > c and c > a):
        print(f"b vale {b} ")
        print(f"c vale {c} ")
        print(f"a vale {a} \n")


    elif (c > a and c > b and a > b):
        print(f"c vale {c} ")
        print(f"a vale {a} ")
        print(f"b vale {b} \n")
    elif (c > a and c > b and b > a):
        print(f"c vale {c} ")
        print(f"b vale {b} ")
        print(f"a vale {a} \n")
else:
    #maior no meio
    if (a > b and a > c and b > c):
        print(f"b vale {b} ")
        print(f"a vale {a} ")
        print(f"c vale {c} \n")
    elif (a > b and a > c and c > b):
        print(f"c vale {c} ")
        print(f"a vale {a} ")
        print(f"d vale {b} \n")
    elif (b > a and b > c and a >c):
        print(f"a vale {a} ")
        print(f"b vale {b} ")
        print(f"c vale {c} \n")
    elif (b > a and b > c and c > a):
        print(f"c vale {c} ")
        print(f"b vale {b} ")
        print(f"a vale {a} \n")
    elif (c > a and c > b and a > b):
        print(f"a vale {a} ")
        print(f"c vale {c} ")
        print(f"b vale {b} \n")
    elif (c > a and c > b and b > a):
        print(f"b vale {b} ")
        print(f"c vale {c} ")
        print(f"a vale {a} \n")