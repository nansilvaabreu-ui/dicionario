aluno = {"nome":"Ana","nota": 8, "cel":"11989891919"}

clientes = [
    {"nome":"Ana", "cel":"11878", "empresa":"FIAT"},
    {"nome":"Pedro", "cel":"11657", "empresa":"INTEL"},
    {"nome":"Maria", "cel":"1176632", "empresa":"SEBRAE"},
    {"nome":"Felipe", "cel":"117468", "empresa":"Microsoft"}
]

pergunta = input("Escolha a empresa: ").upper()

for cliente in clientes:
    if cliente["empresa"] == pergunta:
        print(cliente)

# #cadastrar um novo cliente

print ("---> Cadastrando um novo Cliente <---")
nome = input("Digite o nome do cliente: ")
celular = input("Digite o numero de celular do cliente: ")
empresa = input("Digite a empresa do cliente: ")

novo_cliente = {
    "nome": nome,
    "cel": celular,
    "empresa": empresa
}

clientes.append(novo_cliente)
print(clientes)

#Remover um cliente

print("---> Removendo Cliente <---")
remover = input("Qual cliente deseja remover? ")

for cliente in clientes:
    if cliente["nome"] == remover:
        clientes.remove(cliente)
        break

print(clientes)
    