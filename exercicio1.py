def main():
    contatos = {}
    print("--- Sistema de Agenda ---")
    print("Para encerrar o cadastro, deixe a chave em branco e aperte ENTER.\n")

    while True:
        identificador = input("Chave de Identificação: ").strip()
        if not identificador:
            break

        nome = input("Nome do Contato: ")
        idade = int(input("Idade: "))
        telefone = input("Número de Telefone: ")

        # Alteração na estrutura: usando um dicionário interno para armazenar os dados de forma mais limpa
        contatos[identificador] = {'nome': nome, 'idade': idade, 'telefone': telefone}
        print("-" * 45)

    print("\n=== LISTA DE CONTATOS CADASTRADOS ===")
    for chave, dados in contatos.items():
        print(f"{chave}: {dados['nome']}-{dados['idade']}-{dados['telefone']}")

if __name__ == "__main__":
    main()
