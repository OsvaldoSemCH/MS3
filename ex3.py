## https://github.com/Andredev-dias/Base-de-algoritmos-em-C-v3/blob/master/trabalho_moldularizacao.c

def calculo(p_n1 : float, p_n2 : float, p_n3 : float, p_n4 : float):
    return ((p_n1 + p_n2 + p_n3 + p_n4) / 4)
    
def mostra(p_nome : str, p_mat : int, p_media : float):
    print(f"O aluno(a) {p_nome} com matrícula {p_mat} tem {p_media} de média.\n\n")

mat = int(input("QUAL SUA MATRÍCULA: "))