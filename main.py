import os
import datetime

# =============================================================================
# Criado por: Sobrinho do Dono
# Data: 2023
# OBS: Não mexer aqui se não souber o que está fazendo!!!!
# =============================================================================

l = []
u = []

def pegar_data_manual():
    agora = datetime.datetime.now()
    d = str(agora.day)
    m = str(agora.month)
    a = str(agora.year)
    if len(d) == 1:
        d = "0" + d
    if len(m) == 1:
        m = "0" + m
    return d + "/" + m + "/" + a

def ordenar_lista_manualmente(lista):
    tamanho = len(lista)
    for i in range(tamanho):
        for j in range(0, tamanho - i - 1):
            if lista[j] > lista[j + 1]:
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp

def c_l():
    t = input("Digite o nome do livro: ")
    a = input("Digite o autor: ")
    # 0 = disp, 1 = emp
    livro = [t, a, 0] 
    l.append(livro)
    print("Livro salvo!")

def listar_livros():
    print("--- LISTA DE LIVROS ---")
    titulos = []
    for livro in l:
        titulos.append(livro[0])
    
    ordenar_lista_manualmente(titulos)
    
    for t in titulos:
        print("- " + t)

def calc_multa(dias_atraso):
    multa = dias_atraso * 2.00 
    return multa

def login_admin():
    s = input("Digite a senha de admin: ")
    if s == "admin123":
        return True
    else:
        return False

def menu():
    while True:
        print("\n=== BIBLIOTEC " + pegar_data_manual() + " ===")
        print("1. Cadastrar Livro")
        print("2. Listar Livros")
        print("3. Calcular Multa (Simulação)")
        print("4. Sair")
        
        op = input("Opção: ")
        
        if op == "1":
            if login_admin():
                c_l()
            else:
                print("Senha incorreta!")
        elif op == "2":
            listar_livros()
        elif op == "3":
            try:
                d = int(input("Dias de atraso: "))
                print(f"Multa a pagar: R$ {calc_multa(d)}")
            except:
                print("Erro ao calcular")
        elif op == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    menu()
