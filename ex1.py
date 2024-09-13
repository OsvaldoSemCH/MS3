## https://github.com/Andredev-dias/Base-de-algoritmos-em-C-v3/blob/master/EX_01.c

def Sal_Bruto(p_horasn : float, p_horase : float):
    return ((p_horasn * 12) + (p_horase * 15.5))

def Sal_Liquido(p_respbruto : float):
    return (p_respbruto * 0.9)

def mostra(p_cod, p_horasn, p_horase, p_respbruto, p_respliquido):
    print(f"O funcionário {p_cod} trabalhou {round(p_horasn)} horas normais e {round(p_horase)} horas extras.")
    print(f"Irá receber R$ {round(p_respbruto, 2)} de salário bruto e R$ {round(p_respliquido, 2)} de salário liquido.\n\n")

for cont in range(1, 11):
    cod = int(input("QUAL SEU CODIGO: "))

    horasn = float(input("QUANTIDADE DE HORAS NORMAIS: "))

    horase = float(input("QUANTIDADE DE HORAS EXTRAS: "))

    print("_________________________________________")
    print(f"\n{cont}º FUNCIONARIO CALCULADO: ")
    respbruto = Sal_Bruto(horasn, horase)
    mostra(cod, horasn, horase, respbruto, Sal_Liquido(respbruto))