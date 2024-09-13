## https://github.com/Andredev-dias/Base-de-algoritmos-em-C-v3/blob/master/recursividade2lista.c

def N(p_num):
    acumulo = 0
    if(p_num > 0):
        print(f"{p_num} é um dos números.")
        acumulo = N(p_num - 1) + p_num
    return acumulo

num = input("INFORME UM NUMERO INTEIRO POSITIVO: ")

print(f"{N(num)} é o somatório dos números")