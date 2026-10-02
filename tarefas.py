tarefas = [
    {"titulo": "Estudar", "concluida": "sim", "Prioridade": "alta"},
    {"titulo": "Ler", "concluida": "não", "Prioridade": "baixa"},
    {"titulo": "Lavar o carro", "concluida": "sim", "Prioridade": "baixa"},
    {"titulo": "Arrumar a casa", "concluida": "não", "Prioridade": "alta"}
]


def mostrar_todas():
    print("---> Todas as tarefas <---")

    for tarefa in tarefas:
        print(tarefa)


def mostrar_concluidas():
    print("---> Tarefas concluídas <---")

    for tarefa in tarefas:
        if tarefa["concluida"] == "sim":
            print(tarefa)


def mostrar_pendentes():
    print("---> Tarefas pendentes <---")

    for tarefa in tarefas:
        if tarefa["concluida"] == "não":
            print(tarefa)


def mostrar_prioridades():
    print("---> Tarefas de prioridade ALTA <---")

    for tarefa in tarefas:
        if tarefa["Prioridade"] == "alta":
            print(tarefa)

    print("---> Tarefas de prioridade BAIXA <---")

    for tarefa in tarefas:
        if tarefa["Prioridade"] == "baixa":
            print(tarefa)


def cadastrar_tarefa():
    print("---> Cadastrando nova tarefa <---")

    titulo_tarefa = input("Digite a nova tarefa: ")
    estado = input("Esta tarefa já foi concluída? ")
    prioridade = input("Esta tarefa é de ALTA ou BAIXA prioridade? ")

    nova_tarefa = {
        "titulo": titulo_tarefa,
        "concluida": estado,
        "Prioridade": prioridade
    }

    tarefas.append(nova_tarefa)

    print("Tarefa adicionada!")


def finalizar_tarefa():
    print("---> Finalizando tarefa <---")

    nome_tarefa = input("Qual tarefa deseja finalizar? ")

    for tarefa in tarefas:
        if tarefa["titulo"] == nome_tarefa:
            tarefa["concluida"] = "sim"
            print(f"A tarefa '{nome_tarefa}' foi concluída!")
            return

    print("Tarefa não encontrada.")


def remover_tarefa():
    print("---> Removendo tarefa <---")

    remover = input("Qual tarefa deseja remover? ")

    for tarefa in tarefas:
        if tarefa["titulo"] == remover:
            tarefas.remove(tarefa)
            print(f"A tarefa '{remover}' foi removida!")
            return

    print("Tarefa não encontrada.")


while True:

    print("# LISTA DE TAREFAS #")
    print("1 - Mostrar todas as tarefas")
    print("2 - Mostrar tarefas concluídas")
    print("3 - Mostrar tarefas pendentes")
    print("4 - Mostrar tarefas por prioridade")
    print("5 - Cadastrar tarefa nova")
    print("6 - Finalizar tarefa")
    print("7 - Remover tarefa")
    print("0 - Sair")

    opcao = int(input("Escolha a opção: "))

    if opcao == 1:
        mostrar_todas()

    elif opcao == 2:
        mostrar_concluidas()

    elif opcao == 3:
        mostrar_pendentes()

    elif opcao == 4:
        mostrar_prioridades()

    elif opcao == 5:
        cadastrar_tarefa()

    elif opcao == 6:
        finalizar_tarefa()

    elif opcao == 7:
        remover_tarefa()

    elif opcao == 0:
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida!")