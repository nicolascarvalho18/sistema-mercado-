# Classe para os Produtos
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
        return f"Produto: {self.nome}, Preço: {self.preco:.2f}, Quantidade em estoque: {self.quantidade}"

# Classe para o Mercado
class Mercado:
    def __init__(self):
        self.produtos = {}  # Dicionário para armazenar produtos

    # Função para adicionar um produto
    def adicionar_produto(self, nome, preco, quantidade):
        if nome in self.produtos:
            self.produtos[nome].quantidade += quantidade
        else:
            self.produtos[nome] = Produto(nome, preco, quantidade)
        print(f"Produto {nome} adicionado/atualizado com sucesso!")

    # Função para exibir o estoque
    def exibir_estoque(self):
        print("\nEstoque Atual:")
        for produto in self.produtos.values():
            print(produto)

    # Função para realizar uma venda
    def vender_produto(self, nome, quantidade):
        if nome in self.produtos and self.produtos[nome].quantidade >= quantidade:
            self.produtos[nome].quantidade -= quantidade
            total = self.produtos[nome].preco * quantidade
            print(f"Venda realizada: {quantidade}x {nome} - Total: R${total:.2f}")
            if self.produtos[nome].quantidade == 0:
                del self.produtos[nome]
        else:
            print(f"Produto {nome} não disponível ou quantidade insuficiente.")

    # Função para gerar relatório de vendas
    def relatorio_estoque(self):
        print("\nRelatório de Estoque:")
        for produto in self.produtos.values():
            print(produto)

# Exemplo de Uso
mercado = Mercado()

# Adicionar produtos ao mercado
mercado.adicionar_produto("Arroz", 20.0, 50)
mercado.adicionar_produto("Feijão", 10.0, 30)
mercado.adicionar_produto("Macarrão", 5.0, 100)

# Exibir estoque
mercado.exibir_estoque()

# Realizar uma venda
mercado.vender_produto("Arroz", 10)

# Exibir estoque atualizado
mercado.exibir_estoque()

# Gerar relatório de estoque
mercado.relatorio_estoque()
