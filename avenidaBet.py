nomes = []
apostas = []
valores = []

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
        if not partes[0].strip().isdigit or not partes[1].strip().isdigit:
            print("Informe somente números no placar!")
            continue
        break

    valor = float(input("Valor da Aposta R$: "))

    nomes.append(nome)
    apostas.append(aposta)
    valores.append(valor)


while (True):

    titulo("AvenidaBest - Controle de Aposta\nCaxias x Grêmio (Final do Gauchão 2023)","=")
    
    print("1. Cadastrar Aposta")
    print("2. Listar Aposta")
    print("3. Listar Resultado")
    print("4. Total de Aposta")
    print("5. Aposta por Resultado")
    print("6. Resultado e Premiação")
    print("7. Premiação")

    opcao = int(input("Qual opção deseja: "))

    if opcao == 1:
        incluir()




