# Equipe Antares, Departamento de Avionica
# Instrucoes:
# Para cada vetor a ser testado, incluir no arquivo "alturas.csv"
# uma linha contendo os elementos separados por virgulas sem espacos.
# Os elementos podem ser inteiros ou floats.

import csv

alturas = []

# Abre o arquivo contendo as alturas a serem testadas
with open('alturas.csv') as csvfile:

    # Le o arquivo separando cada elemento do vetor por virgulas
    arq = csv.reader(csvfile, delimiter=',')

    # Insere os elementos do arquivo na lista
    for altura in arq:
        alturas.append(altura)

# Cada linha da matriz representa uma linha do arquivo, e cada coluna representa um elemento daquela linha no arquivo
#Determinacao da condicao de parada 1
# i deve comecar em 1 para nao acessar regioes fora do array
for j in range(0, len(alturas)):
    count = 0
    print ""
    print "Vetor de testes: ", j
    print alturas[j]
    for i in range(1, len(alturas[j])):
        # calcula a diferenca dos ultimos dois valores
        diff = float(alturas[j][i]) - float(alturas[j][i - 1])
        # se a diferenca for negativa, significa que o foguete pode estar em queda, portanto adiciona o contador
        if diff < 0:
            count += 1
        # se nao, alarme falso, ele ainda esta subindo, zera o contador
        else:
            count = 0

        # se tivermos 5 medidas negativas consecutivas, o foguete esta em queda
        if count == 4:
            #Envia sinal GPIO para porta indicando o acionamento do circuito que abre o paraquedas
            print "Abertura do paraquedas na iteracao: ", i
            # sai do loop
            break

        if i == len(alturas[j])-1:
            print "O paraquedas nao abriu"
