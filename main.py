# -*- coding: utf-8 -*-

# Função para classificar o solo
def classificar_solo(peneira_200, peneira_04,ll,ip):

    if peneira_200 <= 50:
        print("Solo Grosso")
        if peneira_04 >= 50:
            print("Areia")
        else:
            print("Pedregulho")
    else:
        print("Solo Fino")

    ipa = 0.73*(ll - peneira_04)

    if ip > ipa:
        print(ipa, "está acima da linha A, logo o solo é Argiloso")
    else:
        print(ipa, "está anbaixo da linha A, logo o solo é Siltoso")
    
# Função para obter dados do usuário e classificar o solo
def obter_dados_usuario():
    try:
        peneira_200 = float(input("Percentual que passa na peneira 200: "))
        peneira_04 = float(input("Percentual que passa na peneira 4: "))
        ll = float(input("limite de liquidez: "))
        ip = float(input("Índice de plasticidade: "))

        classificacao = classificar_solo(peneira_200, peneira_04,ll,ip)

        print(classificacao)
        
    except ValueError as e:
        print("Erro: %s" % e)

# Chama a função para obter dados do usuário e classificar o solo
obter_dados_usuario()