import time
import json

estoque = []


ARQUIVO_PRODUTOS = "produtos.json"



def carregar_produtos():
    try:
        with open(ARQUIVO_PRODUTOS, "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []



def salvar_produtos(produtos):
    with open(ARQUIVO_PRODUTOS, "w") as arquivo:
        json.dump(produtos, arquivo, indent=4)



def main():
    produtos = carregar_produtos()

    while True:
        print("        Gerenciador de estoque    ")

        opcoes = int(input("""        Digite [ 1 ] para adicionar produto(s)
        Digite [ 2 ] para remover produto(s)
        Digite [ 3 ] para consultar estoque
        Digite [ 4 ] para atualizar estoque
        Digite [ 5 ] para sair do programa
        Digite [ 6 ] informações sobre o programa
        Digite a sua opção:"""))

        if opcoes == 1:

            if opcoes == 0:
                print("Voltando ao menu principal...")
                time.sleep(0.5)
                continue

            nome = input("digite [ 0 ] para voltar ao menu principal \nDigite o nome do produto que vai ser adicionado:")
            categoria = input("Categoria do produto:")
            quantidade = int(input("Quantidade:"))
            preco = float(input("Preço R$"))

            produto = {
                "nome": nome,
                "categoria": categoria,
                "quantidade": quantidade,
                "preco": preco
            }
            produtos.append(produto)
            salvar_produtos(produtos)

            time.sleep(0.5)

            print("=-=" * 10)
            print("Produto adicionado com sucesso!")
            print("=-=" * 10)

        elif opcoes == 2:
            print("Qual item deseja remover?  (Ou Digite [ 0 ] para voltar ao menu principal):")
            if not produtos:
                print("O estoque está vazio!")
                continue

            for indice, produto in enumerate(produtos, start=1):
                print(f"[{indice}] {produto['nome']} - {produto['quantidade']} unidades")

            try:
                escolha = int(input("Digite o número do produto para remover ou [ 0 ] para voltar: "))
                if escolha == 0:
                    print("Voltando ao menu principal...")
                    time.sleep(3)
                    continue
                elif 1 <= escolha <= len(produtos):
                    produto_remover = produtos[escolha - 1]
                    produtos.remove(produto_remover)
                    salvar_produtos(produtos)
                    print("Produto removido com sucesso!")
                else:
                    print("Produto inválido.")
            except ValueError:
                print("Opção inválida.")


        elif opcoes == 3:
            if not produtos:
                print("O estoque está vazio.")
            else:
                print("Produtos no estoque:")
                for produto in produtos:
                    print(
                        f"\nNome: {produto['nome']} \nCategoria: {produto['categoria']} \nQuantidade: {produto['quantidade']} \nPreço: R${produto['preco']:.2f}")

            try:
                opcao = int(input("Digite [ 0 ] para sair da consulta de estoque: "))
                if opcao == 0:
                    print("Saindo da consulta de estoque...")
                    time.sleep(3)
                    continue
            except ValueError:
                print("Comando inválido")

        elif opcoes == 4:
            if not produtos:
                print("O estoque está vazio. Não há nada para atualizar.")
                continue

            for indice, produto in enumerate(produtos, start=1):
                print(f"[{indice}] Nome: {produto['nome']} \nCategoria: {produto['categoria']} \nQuantidade: {produto['quantidade']} \nPreço: R${produto['preco']:.2f}")

            try:
                escolha = int(input("Digite o número do produto que deseja atualizar ou [ 0 ] para voltar ao menu principal: "))
                if escolha == 0:
                    print("Voltando ao menu principal...")
                    time.sleep(3)
                    continue
                elif 1 <= escolha <= len(produtos):
                    produto_atualizar = produtos[escolha - 1]

                else:
                    print("Número do produto inválido.")
            except ValueError:
                print("Por favor, digite um número válido.")


        elif opcoes == 5:
            print("Saindo do programa...")
            time.sleep(3)
            print("Até mais!")
            break

        elif opcoes == 6:
            print(" 2024 \nGerenciador de estoque versão 1.0 \nCriado por Julio Cesar Splendor")


if __name__ == "__main__":
    main()



        #4. return
# A return é usada dentro de funções para devolver um valor como resultado da execução da função.
# Sem ela, a função não retorna nada (ou retorna None por padrão).
# Exemplo:

# python
# Copiar código
# def soma(a, b):
    # return a + b  # Retorna a soma dos dois números

# resultado = soma(3, 5)
# print(resultado)  # Saída: 8
# Dica: Use return sempre que precisar de um valor que será usado fora da função.
# 5. main()
# O main() é apenas uma convenção em Python para definir o ponto de entrada principal de um programa. Ele é frequentemente usado junto com a verificação especial:
# python
# Copiar código
# if __name__ == "__main__":
   # main()
# O que isso faz?

# Quando o arquivo é executado diretamente, o bloco if __name__ == "__main__" será executado.
# Se o arquivo for importado como um módulo, esse bloco não será executado.
# Exemplo:

# python
# Copiar código
# def main():
   # print("Executando o programa principal!")

# if __name__ == "__main__":
   # main()
# Esse formato é útil em projetos maiores para organizar melhor o código.
