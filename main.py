from hospede import Hospede
from funcionario import Gerente, Recepcionista, TecnicoManutencao
from tecnico_recepcao import TecnicoRecepcao
from quarto import QuartoSimples, QuartoLuxo

quartos = []
hospedes = []
funcionarios = []

def criar_quarto():
    print("\n--- CRIAR QUARTO ---")
    numero_str = input("Número do quarto: ")
    if not numero_str.isdigit():
        print("Número inválido!")
        return
    numero = int(numero_str)

    for quarto in quartos:
        if quarto.numero == numero:
            print("Já existe um quarto com esse número!")
            return

    print("1 - Simples\n2 - Luxo")
    tipo = input("Escolha o tipo: ")
    
    preco = float(input("Preço por dia (€): "))
    if preco < 0:
        print("Preço não pode ser negativo!")
        return

    if tipo == "1":
        quarto = QuartoSimples(numero, preco)
    elif tipo == "2":
        quarto = QuartoLuxo(numero, preco)
    else:
        print("Tipo inválido!")
        return

    quartos.append(quarto)
    print("Quarto criado com sucesso!")


def listar_quartos():
    print("\n--- LISTA DE QUARTOS ---")
    if not quartos:
        print("Não existem quartos registados.")
        return

    for quarto in quartos:
        quarto.mostrar_informacoes()


def criar_hospede():
    print("\n--- REGISTAR HÓSPEDE ---")
    nome = input("Nome: ")

    idade_str = input("Idade: ")
    if not idade_str.isdigit():
        print("Idade inválida!")
        return
    idade = int(idade_str)
    if idade <= 0:
        print("Idade inválida!")
        return

    dias_str = input("Dias de estadia: ")
    if not dias_str.isdigit():
        print("Dias de estadia inválidos!")
        return
    dias_estadia = int(dias_str)
    if dias_estadia <= 0:
        print("Dias de estadia inválidos!")
        return

    if not quartos:
        print("Não existem quartos disponíveis no hotel!")
        return

    print("\nQuartos Existentes:")
    for quarto in quartos:
        quarto.mostrar_informacoes()

    numero_str = input("\nNúmero do quarto para alojar: ")
    if not numero_str.isdigit():
        print("Número inválido!")
        return
    numero = int(numero_str)

    quarto_escolhido = None
    for quarto in quartos:
        if quarto.numero == numero:
            quarto_escolhido = quarto
            break

    if quarto_escolhido is None:
        print("Quarto não encontrado!")
        return

    if quarto_escolhido.ocupado:
        print("O quarto selecionado já está ocupado!")
        return

    hospede = Hospede(nome, idade, dias_estadia, quarto_escolhido)
    hospedes.append(hospede)
    print("Hóspede registado com sucesso!")


def listar_hospedes():
    print("\n--- LISTA DE HÓSPEDES ---")
    if not hospedes:
        print("Não existem hóspedes registados.")
        return

    for hospede in hospedes:
        hospede.mostrar_informacoes()
        print(f"Valor Total da Conta: {hospede.calcular_conta():.2f}€")
        print("-" * 35)


def fazer_checkout():
    print("\n--- CHECKOUT ---")
    nome = input("Nome do hóspede: ")

    hospede_encontrado = None
    for hospede in hospedes:
        if hospede.nome.lower() == nome.lower():
            hospede_encontrado = hospede
            break

    if hospede_encontrado is None:
        print("Hóspede não encontrado!")
        return

    print(f"Valor total a pagar: {hospede_encontrado.calcular_conta():.2f}€")
    hospede_encontrado.checkout()
    hospedes.remove(hospede_encontrado)


def criar_funcionario():
    print("\n--- CRIAR FUNCIONÁRIO ---")
    print("1 - Gerente\n2 - Recepcionista\n3 - Técnico de Manutenção\n4 - Técnico de Receção")

    opcao = input("Escolha uma opção: ")
    if opcao not in ["1", "2", "3", "4"]:
        print("Opção inválida!")
        return

    nome = input("Nome: ")
    
    idade_str = input("Idade: ")
    if not idade_str.isdigit():
        print("Idade inválida!")
        return
    idade = int(idade_str)
    if idade <= 0:
        print("Idade inválida!")
        return

    salario = float(input("Salário (€): "))
    if salario <= 0:
        print("Salário inválido!")
        return

    if opcao == "1":
        bonus = float(input("Bónus (€): "))
        if bonus < 0:
            print("Bónus inválido!")
            return
        funcionario = Gerente(nome, idade, salario, bonus)

    elif opcao == "2":
        id_str = input("ID do funcionário: ")
        if not id_str.isdigit():
            print("ID inválido!")
            return
        id_func = int(id_str)
        if id_func <= 0:
            print("ID inválido!")
            return

        for f in funcionarios:
            if hasattr(f, 'id_func') and f.id_func == id_func:
                print("Já existe um funcionário com esse ID!")
                return

        turno = input("Turno (manhã/tarde/noite): ")
        funcionario = Recepcionista(nome, id_func, idade, salario, turno)

    elif opcao == "3":
        especialidade = input("Especialidade: ")
        funcionario = TecnicoManutencao(nome, idade, salario, especialidade)

    elif opcao == "4":
        id_str = input("ID do funcionário: ")
        if not id_str.isdigit():
            print("ID inválido!")
            return
        id_func = int(id_str)
        if id_func <= 0:
            print("ID inválido!")
            return

        for f in funcionarios:
            if hasattr(f, 'id_func') and f.id_func == id_func:
                print("Já existe um funcionário com esse ID!")
                return

        setor = input("Setor: ")
        especialidade = input("Especialidade: ")
        funcionario = TecnicoRecepcao(nome, id_func, idade, salario, setor, especialidade)

    funcionarios.append(funcionario)
    print("Funcionário criado com sucesso!")


def relatorio():
    print("\n--- RELATÓRIO DO HOTEL ---")
    if not funcionarios:
        print("Não existem funcionários registados.")
        return

    gerente = next((f for f in funcionarios if isinstance(f, Gerente)), None)
    if gerente:
        gerente.gerar_relatorio(funcionarios)
    else:
        for f in funcionarios:
            f.mostrar_informacoes()


def registrar_reparo():
    print("\n--- REGISTAR REPARO ---")
    descricao = input("Descrição do reparo: ")
    tecnicos = [f for f in funcionarios if isinstance(f, TecnicoManutencao)]

    if not tecnicos:
        print("Não existem técnicos registados no sistema!")
        return

    for i, tecnico in enumerate(tecnicos):
        print(f"{i + 1} - {tecnico.nome} ({tecnico.__class__.__name__})")

    escolha_str = input("Escolha o técnico: ")
    if not escolha_str.isdigit():
        print("Opção inválida!")
        return
    escolha = int(escolha_str)

    if escolha < 1 or escolha > len(tecnicos):
        print("Opção inválida!")
        return

    tecnicos[escolha - 1].registar_reparo(descricao)



while True:
    print("\n===== GESTÃO DO HOTEL =====")
    print("1 - Criar quarto")
    print("2 - Listar quartos")
    print("3 - Registar hóspede")
    print("4 - Listar hóspedes")
    print("5 - Fazer checkout")
    print("6 - Criar funcionário")
    print("7 - Imprimir relatório")
    print("8 - Registar reparo")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        criar_quarto()
    elif opcao == "2":
        listar_quartos()
    elif opcao == "3":
        criar_hospede()
    elif opcao == "4":
        listar_hospedes()
    elif opcao == "5":
        fazer_checkout()
    elif opcao == "6":
        criar_funcionario()
    elif opcao == "7":
        relatorio()
    elif opcao == "8":
        registrar_reparo()
    elif opcao == "0":
        print("A encerrar o sistema do hotel... Até breve!")
        break
    else:
        print("Opção inválida! Tente novamente.")