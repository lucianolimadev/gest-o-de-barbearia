from collections import deque

SERVICOS = {
    1: ("Corte", 35.0),
    2: ("Barba", 25.0),
    3: ("Sobrancelha", 15.0),
    4: ("Lavagem", 20.0),
    5: ("Pigmentação", 30.0),
}

LIMITE_CLIENTES = 20
1
fila_clientes = deque()
clientes_atendidos = 0
quantidade_servicos_realizados = 0
valor_faturado = 0.0


def mostrar_servicos():
    print("\nServiços disponíveis:")
    for codigo, (nome, preco) in SERVICOS.items():
        print(f"{codigo} - {nome} | R$ {preco:.2f}")


def cadastrar_cliente():
    if len(fila_clientes) >= LIMITE_CLIENTES:
        print("\nFila lotada. O sistema permite no máximo 20 clientes.")
        return

    nome = input("\nNome do cliente: ").strip()
    if not nome:
        print("Nome inválido.")
        return

    mostrar_servicos()
    print("Digite os códigos dos serviços separados por vírgula. Ex.: 1,2,4")
    entrada = input("Serviços desejados: ").strip()

    if not entrada:
        print("O cliente precisa escolher pelo menos 1 serviço.")
        return

    try:
        codigos = [int(item.strip()) for item in entrada.split(",")]
    except ValueError:
        print("Entrada inválida. Informe apenas números separados por vírgula.")
        return

    servicos_escolhidos = []
    for codigo in codigos:
        if codigo not in SERVICOS:
            print(f"Serviço código {codigo} não existe.")
            return
        servicos_escolhidos.append(SERVICOS[codigo])

    total = sum(preco for _, preco in servicos_escolhidos)
    fila_clientes.append({
        "nome": nome,
        "servicos": servicos_escolhidos,
        "total": total,
    })

    print(f"\nCliente {nome} adicionado à fila com sucesso.")
    print(f"Total a pagar: R$ {total:.2f}")
    print(f"Clientes na fila: {len(fila_clientes)}/{LIMITE_CLIENTES}")


def listar_fila():
    if not fila_clientes:
        print("\nNão há clientes na fila.")
        return

    print("\nFila de clientes:")
    for posicao, cliente in enumerate(fila_clientes, start=1):
        nomes_servicos = ", ".join(nome for nome, _ in cliente["servicos"])
        print(f"{posicao}. {cliente['nome']} -> {nomes_servicos} | R$ {cliente['total']:.2f}")


def chamar_cliente():
    global clientes_atendidos, quantidade_servicos_realizados, valor_faturado

    if not fila_clientes:
        print("\nNão há clientes para atender.")
        return

    cliente = fila_clientes.popleft()
    clientes_atendidos += 1
    quantidade_servicos_realizados += len(cliente["servicos"])
    valor_faturado += cliente["total"]

    print("\nCliente chamado na ordem da fila:")
    print(f"Nome: {cliente['nome']}")
    print("Serviços realizados:")
    for nome, preco in cliente["servicos"]:
        print(f"- {nome} | R$ {preco:.2f}")
    print(f"Total do atendimento: R$ {cliente['total']:.2f}")


def mostrar_relatorio_final():
    print("\n===== RELATÓRIO FINAL =====")
    print(f"Quantidade de serviços realizados: {quantidade_servicos_realizados}")
    print(f"Clientes atendidos: {clientes_atendidos}")
    print(f"Valor faturado: R$ {valor_faturado:.2f}")
    print(f"Clientes ainda na fila: {len(fila_clientes)}")


def menu():
    while True:
        print("\n===== SISTEMA DE GESTÃO DE BARBEARIA =====")
        print("1 - Cadastrar cliente na fila")
        print("2 - Listar fila")
        print("3 - Chamar próximo cliente")
        print("4 - Mostrar relatório final")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            listar_fila()
        elif opcao == "3":
            chamar_cliente()
        elif opcao == "4":
            mostrar_relatorio_final()
        elif opcao == "0":
            print("\nEncerrando o sistema...")
            mostrar_relatorio_final()
            break
        else:
            print("\nOpção inválida. Tente novamente.")


# Corrigido com duplo underline de cada lado
if __name__ == "__main__":
    menu()