# -*- coding: utf-8 -*-
import time

# Função para classificar o solo
def classificar_solo(peneira_4200, fracao_grossa, porcentagem_areia, porcentagem_finos, carta_plasticidade=None, Cu=None, Cc=None, IP=None, LL=None):
    if peneira_4200 >= 50:
        if carta_plasticidade is None:
            return "Carta de plasticidade é necessária para classificação quando peneira_4200 é maior ou igual a 50%"
        if IP is None or LL is None:
            return "IP e LL são necessários para classificar solos finos"
        
        if IP > 7:
            compressibilidade = 'L (baixa compressibilidade)' if LL < 50 else 'H (alta compressibilidade)'
            return 'C (argila) com %s' % compressibilidade
        elif IP < 4:
            compressibilidade = 'L (baixa compressibilidade)' if LL < 50 else 'H (alta compressibilidade)'
            return 'M (silte) com %s' % compressibilidade
        else:
            return 'O (orgânico)'
    else:
        if porcentagem_areia >= 50:
            solo_tipo = 'S (areia)'
        else:
            solo_tipo = 'G (pedregulho)'
        
        if porcentagem_finos < 5:
            if Cu is None or Cc is None:
                return "Cu e Cc são necessários para classificar como W ou P"
            classificacao_secundaria = 'W (bem graduado)' if Cu >= 4 and 1 <= Cc <= 3 else 'P (mal graduado)'
        elif porcentagem_finos > 12:
            if IP is None or LL is None:
                return "IP e LL são necessários para classificar como C ou M"
            classificacao_secundaria = 'C (argiloso)' if IP > 7 else 'M (siltoso)'
        else:
            classificacao_secundaria = 'Com ambas características (C e M)'

        return '%s com %s' % (solo_tipo, classificacao_secundaria)

# Função para obter dados do usuário e classificar o solo
def obter_dados_usuario():
    try:
        peneira_4200 = float(input("Percentual que passa na peneira 4200 (0,074 mm): "))
        fracao_grossa = float(input("Percentual da fração grossa (maior que 0,074 mm): "))
        porcentagem_areia = float(input("Percentual de areia da fração grossa: "))
        porcentagem_finos = float(input("Percentual de finos: "))

        if peneira_4200 >= 50:
            carta_plasticidade = input("Carta de plasticidade (se aplicável): ")
            IP = float(input("Índice de plasticidade: "))
            LL = float(input("Limite de liquidez: "))
            classificacao = classificar_solo(peneira_4200, fracao_grossa, porcentagem_areia, porcentagem_finos, carta_plasticidade=carta_plasticidade, IP=IP, LL=LL)
        else:
            Cu = float(input("Coeficiente de uniformidade: "))
            Cc = float(input("Coeficiente de curvatura: "))
            classificacao = classificar_solo(peneira_4200, fracao_grossa, porcentagem_areia, porcentagem_finos, Cu=Cu, Cc=Cc)

        print("Classificação do solo:", classificacao)
        time.sleep(20)

    except ValueError as e:
        print("Erro: %s" % e)

# Chama a função para obter dados do usuário e classificar o solo
obter_dados_usuario()
