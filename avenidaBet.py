import os

nomes = []
apostas = []
valores = []

def obter_dados_do_arquivo():
  # se o arquivo não existe, retorna
  if not os.path.isfile("apostas.txt"):
    return
  
  # abre o arquivo para leitura
  with open("apostas.txt", "r") as arq:
    # lê todas as linhas do arquivo (carregando em um vetor)
    linhas = arq.readlines()

    for linha in linhas:
      # separa a linha em elementos de vetor, a cada ";"
      partes = linha.split(";")
      nomes.append(partes[0])
      apostas.append(partes[1])
      valores.append(float(partes[2][0:-1]))  

def salvar_dados_no_arquivo():
  # abre o arquivo para gravação (sobrepõe os dados)
  with open("apostas.txt", "w") as arq:
    
    for nome, aposta, valor in zip(nomes, apostas, valores):
      arq.write(f"{nome};{aposta};{valor}\n")

def titulo(texto, sublinhado="-"):
    print()
    print(texto)
    print(sublinhado*30)

def incluir():
    titulo("Inclusão de Aposta: Caxias x Grêmio")
    nome = input("Nome do Apostador: ")
    
    while True:
        aposta = input("Aposta (formato 2x1): ").lower()
        partes = aposta.split("x")

        if len(partes) != 2:
            print("Formato Incorreto!")
            continue
        if not partes[0].strip().isdigit() or not partes[1].strip().isdigit():
            print("Informe somente números no placar!")
            continue
        break

    valor = float(input("Valor da Aposta R$: "))

    nomes.append(nome)
    apostas.append(aposta)
    valores.append(valor)

def listar():
    titulo("Listagem das Apostas - Caxias x Grêmio")
    print("Nome do Apsostador ............ Aposta:   Valor R$: ")
    for nome, aposta, valor in zip(nomes, apostas, valores):
        print(f"{nome:30} {aposta:^7} {valor:9.2f}")

def listar_resultado():
    
    titulo("Listagem das Apostas - Caxias x Grêmio")
    print("Nome do Apostador...........  Aposta")

    for nome, aposta in zip(nomes, apostas):
        partes = aposta.split("x")
        if int(partes[0]) > int(partes[1]):
            apostou = "Caxias"
        elif int(partes[0]) == int(partes[1]):
            apostou = "Empate"
        else:
            apostou = "Grêmio"
        print(f"{nome:30} {apostou}")

def totalizar():
    titulo("Listagem das Apostas - Caxias x Grêmio")
    numero_aposta = len(nomes)
    total_dinheiro = sum(valores)
    print("Quantidade de Apostador........... Total Apostado")
    print(f"{numero_aposta} {total_dinheiro:30}")
    
def apostas_resultado():
    titulo("Total de aposta em cada Time - Caxias x Grêmio")
    caxias = 0
    gremio = 0
    empate = 0

    for aposta in zip(apostas):
        partes = aposta.split("x")
        if int(partes[0]) > int(partes[1]):
            caxias = caxias + 1
        elif int(partes[0]) == int(partes[1]):
            empate = empate + 1
        else:
            gremio = gremio + 1
    print("Caxias.....Empate......Grêmio")
    print(f"{caxias} {empate:30} {gremio:60}")

def premiacao():
    titulo("Premiação e Resultados - Caxias x Grêmio")
    campeao = int(input("Qual o resultado da partida(2x1): "))
   

obter_dados_do_arquivo()

while (True):
    titulo("AvenidaBest - Controle de Aposta\nCaxias x Grêmio (Final do Gauchão 2023)","=")
    print("1. Cadastrar Aposta")
    print("2. Listar Aposta")
    print("3. Listar Resultado")
    print("4. Total de Aposta")
    print("5. Aposta por Resultado")
    print("6. Resultado e Premiação")
    print("7. Finalizar")
    print()
    opcao = int(input("Qual opção deseja: "))
    print()
    if opcao == 1:
        incluir()
    elif opcao == 2:
        listar()
    elif opcao == 3:
        listar_resultado()
    elif opcao == 4:
        totalizar()
    elif opcao == 5:
        apostas_resultado()
    elif opcao == 6:
        premiacao()
    else:
        salvar_dados_no_arquivo()
        break
