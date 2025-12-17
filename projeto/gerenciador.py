def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {
        "nome": nome_tarefa,
        "completada": False
    }
    tarefas.append(tarefa)
    print(f"Tarefa '{nome_tarefa}' foi adicionada com sucesso!")


def ver_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    print("\nLista de tarefas:")
    for i, tarefa in enumerate(tarefas, start=1):
        status = "✔" if tarefa["completada"] else "❌"
        print(f"{i}. {tarefa['nome']} - {status}")


# Lista principal
tarefas = []

while True:
    print("\nMENU DO GERENCIADOR DE TAREFAS")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("6. Sair")

    escolha = input("Digite sua escolha: ")

    if escolha == "1":
        nome_tarefa = input("Digite o nome da tarefa: ")
        adicionar_tarefa(tarefas, nome_tarefa)

    elif escolha == "2":
        ver_tarefas(tarefas)

    elif escolha == "6":
        print("Programa finalizado.")
        break

    else:
        print("Opção inválida.")

