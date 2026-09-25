tarefas =[
    {"titulo":"Estudar", "concluida":"sim", "Prioridade":"alta"},
    {"titulo":"Ler", "concluida":"não", "Prioridade":"baixa"},
    {"titulo":"Lavar o carro", "concluida":"sim", "Prioridade":"baixa"},
    {"titulo":"Arrumar a casa", "concluida":"não", "Prioridade":"alta"}
]

print("# LISTA DE TAREFAS #")
print("1 - Mostrar todas as tarefas")
print("2 - Mostar tarefas concluidas")
print("3 - Mostrar tarefas pendentes")
print("4 - Mostrar tarefas por prioridade")
print("5 - Cadastrar tarefa nova")
print("6 - Finalizar tarefa")
print("7 - Remover tarefa")
print("0 - Sair")

opcao = int(input("Escolha a opção: "))

if opcao == 1:
    print(tarefas)

elif opcao == 2:
    for concluida in tarefas:
        if concluida["concluida"] == "sim":
            print(concluida)
elif opcao == 3:
    for pendente in tarefas:
        if pendente["concluida"] == "não":
            print(pendente)
elif opcao == 4:
    print("Tarefas de prioridade ALTA:")
    for tarefa in tarefas:
        if tarefa["Prioridade"] == "alta":
            print(tarefa)

    print("Tarefas de prioridade BAIXA:")

    for tarefa in tarefas:
        if tarefa["Prioridade"] == "baixa":
            print(tarefa)
elif opcao == 5:
    print ("---> Cadastrando nova Tarefa <---")
    titulo_tarefa = input("Digite a nova tarefa: ")
    estado = input("Esta tarefa já foi concluida? ")
    prioridade = input("Esta tarefa é de ALTA ou BAIXA prioridade? ")

    nova_tarefa = {
        "titulo": titulo_tarefa,
        "concluida": estado,
        "Prioridade": prioridade
}
    tarefas.append(nova_tarefa)
    print(tarefas)
    print("Tarefa adicionada!")

elif opcao == 6:
    tarefa = input("Qual tarefa deseja modificar? ")
    modif = input("A tarefa já foi concluída? ")
    for tarefa_modificar in tarefas:
        if tarefa_modificar["titulo"] == tarefa:
            tarefa_modificar["concluida"] = modif
            print(f"Você modificou a tarefa: {tarefa}!")
            break
    print(tarefas)

elif opcao == 7:
    
    print("---> Removendo Tarefa <---")
remover = input("Qual tarefa deseja remover? ")

for remover_tarefa in tarefas:
    if remover_tarefa["titulo"] == remover:
        tarefas.remove(remover_tarefa)
        break

print(tarefas)
print("Tarefa removida!!")
    