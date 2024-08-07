# -*- coding: utf-8 -*-
import os

# Função para classificar o solo
def classificar_solo(peneira_200, peneira_04, ll, ip):
    ipa = 0.73 * (ll - 20)
    resultado = []

    if peneira_200 <= 50:
        resultado.append("Solo Grosso")
        
        if peneira_200 > 12:
            if peneira_04 >= 50:
                if ip > ipa:
                    resultado.append(f"{ipa:.2f} está acima da linha A, logo o solo é Areia Argiloso")
                else:
                    resultado.append(f"{ipa:.2f} está abaixo da linha A, logo o solo é Areia Siltoso")
            else:
                resultado.append("Pedregulho")
                if ip > ipa:
                    resultado.append(f"{ipa:.2f} está acima da linha A, logo o solo é Pedregulho Argiloso")
                else:
                    resultado.append(f"{ipa:.2f} está abaixo da linha A, logo o solo é Pedregulho Siltoso")
        elif peneira_200 < 5:
            cc = float(input("Índice de CC: "))
            cu = float(input("Índice de CU: "))

            if peneira_04 >= 50:
                if cu >= 4 and 1<=cc<=3:
                    resultado.append("Areia bem graduado")
                else:
                    resultado.append("Areia mal graduado")
            else:
                if cu >= 4 and 1<=cc<=3:
                    resultado.append("Pedregulho bem graduado")
                else:
                    resultado.append("Pedregulho mal graduado")  

        else:
            cc = float(input("Índice de CC: "))
            cu = float(input("Índice de CU: "))

            if peneira_04 >= 50:
                if ip > ipa:
                    resultado.append(f"{ipa:.2f} está acima da linha A, logo o solo é Areia Argiloso")
                else:
                    resultado.append(f"{ipa:.2f} está abaixo da linha A, logo o solo é Areia Siltoso")
            else:
                resultado.append("Pedregulho")
                if ip > ipa:
                    resultado.append(f"{ipa:.2f} está acima da linha A, logo o solo é Pedregulho Argiloso")
                else:
                    resultado.append(f"{ipa:.2f} está abaixo da linha A, logo o solo é Pedregulho Siltoso")

            if peneira_04 >= 50:
                if cu >= 4 and 1<=cc<=3:
                    resultado.append("Areia bem graduado")
                else:
                    resultado.append("Areia mal graduado")
            else:
                if cu >= 4 and 1<=cc<=3:
                    resultado.append("Pedregulho bem graduado")
                else:
                    resultado.append("Pedregulho mal graduado") 
            
    else:
        resultado.append("Solo Fino")
        if ll >= 50:
            resultado.append("Alta compressibilidade")
            if ip > ipa:
                resultado.append(f"{ipa:.2f} está acima da linha A, logo o solo é Argila")
            else:
                resultado.append(f"{ipa:.2f} está abaixo da linha A, logo o solo é Silte")
        else:
            resultado.append("Baixa compressibilidade")
            if ip > ipa:
                resultado.append(f"{ipa:.2f} está acima da linha A, logo o solo é Argila")
            else:
                resultado.append(f"{ipa:.2f} está abaixo da linha A, logo o solo é Silte")

    return "\n".join(resultado)

# Função para obter dados do usuário e classificar o solo
def obter_dados_usuario():
    while True:
        try:
            peneira_200 = float(input("Percentual que passa na peneira 200: "))
            peneira_04 = float(input("Percentual que passa na peneira 4: "))
            ll = float(input("Limite de liquidez: "))
            ip = float(input("Índice de plasticidade: "))

            classificacao = classificar_solo(peneira_200, peneira_04, ll, ip)

            print("\nClassificação do Solo:")
            print(classificacao)
            
        except ValueError as e:
            print("Erro: %s" % e)

        # Pergunta ao usuário se ele deseja continuar ou sair
        print("\nDeseja continuar ou sair?")
        print("1. Continuar")
        print("2. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '2':
            print("Saindo da aplicação...")
            break
        elif escolha == '1':
            limpar_terminal()
            continue
        else:
            print("Opção inválida. Tente novamente.")

def limpar_terminal():
    os.system('cls')

# Chama a função para obter dados do usuário e classificar o solo
if __name__ == "__main__":
    obter_dados_usuario()
