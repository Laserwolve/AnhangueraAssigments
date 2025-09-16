import matplotlib.pyplot as plt

# Passo 1: Definir a classe Livro
class Livro:
    """
    Classe que representa um livro na biblioteca
    Atributos: titulo, autor, genero, quantidade_disponivel
    """
    def __init__(self, titulo, autor, genero, quantidade_disponivel):
        """
        Construtor da classe Livro
        
        Parametros:
        titulo (str): Titulo do livro
        autor (str): Nome do autor
        genero (str): Genero literario do livro
        quantidade_disponivel (int): Quantidade de exemplares disponiveis
        """
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade_disponivel = quantidade_disponivel
    
    def __str__(self):
        """
        Metodo para representacao em string do objeto Livro
        Retorna informacoes formatadas do livro
        """
        return f"Titulo: {self.titulo} | Autor: {self.autor} | Genero: {self.genero} | Disponivel: {self.quantidade_disponivel}"

# Passo 2: Criar a lista de livros
lista_livros = []

# Passo 3: Implementar funcoes para gerenciar os livros

def cadastrar_livro():
    """
    Funcao para cadastrar um novo livro na biblioteca
    Solicita informacoes do usuario e adiciona o livro na lista
    """
    print("\n=== CADASTRAR NOVO LIVRO ===")
    
    # Coleta informacoes do livro
    titulo = input("Digite o titulo do livro: ").strip()
    autor = input("Digite o nome do autor: ").strip()
    genero = input("Digite o genero do livro: ").strip()
    
    # Valida a quantidade disponivel
    try:
        quantidade = int(input("Digite a quantidade disponivel: "))
        if quantidade < 0:
            print("Erro: A quantidade nao pode ser negativa!")
            return
    except ValueError:
        print("Erro: Digite um numero valido para a quantidade!")
        return
    
    # Verifica se o livro ja existe (mesmo titulo e autor)
    for livro in lista_livros:
        if livro.titulo.lower() == titulo.lower() and livro.autor.lower() == autor.lower():
            # Se existe, atualiza a quantidade
            livro.quantidade_disponivel += quantidade
            print(f"Livro ja existia! Quantidade atualizada para {livro.quantidade_disponivel}")
            return
    
    # Cria novo livro e adiciona na lista
    novo_livro = Livro(titulo, autor, genero, quantidade)
    lista_livros.append(novo_livro)
    print("Livro cadastrado com sucesso!")

def listar_livros():
    """
    Funcao para listar todos os livros disponveis na biblioteca
    Exibe informacoes completas de cada livro
    """
    print("\n=== LISTA DE TODOS OS LIVROS ===")
    
    if not lista_livros:
        print("Nenhum livro cadastrado na biblioteca.")
        return
    
    # Lista todos os livros com numeracao
    for i, livro in enumerate(lista_livros, 1):
        print(f"{i}. {livro}")

def buscar_livro_por_titulo():
    """
    Funcao para buscar um livro pelo titulo
    Permite busca parcial (nao precisa digitar o titulo completo)
    """
    print("\n=== BUSCAR LIVRO POR TITULO ===")
    
    if not lista_livros:
        print("Nenhum livro cadastrado na biblioteca.")
        return
    
    titulo_busca = input("Digite o titulo (ou parte dele) para buscar: ").strip().lower()
    
    # Procura livros que contenham o texto buscado
    livros_encontrados = []
    for livro in lista_livros:
        if titulo_busca in livro.titulo.lower():
            livros_encontrados.append(livro)
    
    # Exibe resultados
    if livros_encontrados:
        print(f"\nEncontrados {len(livros_encontrados)} livro(s):")
        for i, livro in enumerate(livros_encontrados, 1):
            print(f"{i}. {livro}")
    else:
        print("Nenhum livro encontrado com esse titulo.")

# Passo 4: Utilizar a biblioteca Matplotlib para gerar um grafico
def gerar_grafico_por_genero():
    """
    Funcao para gerar grafico de quantidade de livros por genero
    Utiliza matplotlib para criar um grafico de barras
    """
    print("\n=== GERANDO GRAFICO POR GENERO ===")
    
    if not lista_livros:
        print("Nenhum livro cadastrado. Nao e possivel gerar o grafico.")
        return
    
    # Conta livros por genero (considerando quantidade disponivel)
    generos_quantidade = {}
    for livro in lista_livros:
        genero = livro.genero.title()  # Padroniza primeira letra maiuscula
        if genero in generos_quantidade:
            generos_quantidade[genero] += livro.quantidade_disponivel
        else:
            generos_quantidade[genero] = livro.quantidade_disponivel
    
    # Prepara dados para o grafico
    generos = list(generos_quantidade.keys())
    quantidades = list(generos_quantidade.values())
    
    # Cria o grafico
    plt.figure(figsize=(10, 6))
    barras = plt.bar(generos, quantidades, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD', '#98D8C8'])
    
    # Configura o grafico
    plt.title('Quantidade de Livros por Genero', fontsize=16, fontweight='bold')
    plt.xlabel('Genero', fontsize=12)
    plt.ylabel('Quantidade de Livros', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    
    # Adiciona valores nas barras
    for barra, quantidade in zip(barras, quantidades):
        plt.text(barra.get_x() + barra.get_width()/2, barra.get_height() + 0.1, 
                str(quantidade), ha='center', va='bottom', fontweight='bold')
    
    # Ajusta layout e exibe
    plt.tight_layout()
    plt.grid(axis='y', alpha=0.3)
    plt.show()
    
    print("Grafico gerado com sucesso!")

def adicionar_livros_exemplo():
    """
    Funcao para adicionar alguns livros de exemplo para teste
    Facilita o teste do sistema sem precisar cadastrar manualmente
    """
    livros_exemplo = [
        Livro("Dom Casmurro", "Machado de Assis", "Romance", 3),
        Livro("O Cortico", "Aluisio Azevedo", "Realismo", 2),
        Livro("1984", "George Orwell", "Ficcao Cientifica", 4),
        Livro("O Pequeno Principe", "Antoine de Saint-Exupery", "Infantil", 5),
        Livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling", "Fantasia", 3),
        Livro("Sherlock Holmes", "Arthur Conan Doyle", "Misterio", 2),
        Livro("O Senhor dos Aneis", "J.R.R. Tolkien", "Fantasia", 4)
    ]
    
    lista_livros.extend(livros_exemplo)
    print("Livros de exemplo adicionados com sucesso!")

def exibir_menu():
    """
    Funcao que exibe o menu principal do sistema
    Retorna a opcao escolhida pelo usuario
    """
    print("\n" + "="*50)
    print("    SISTEMA DE GERENCIAMENTO DE BIBLIOTECA")
    print("="*50)
    print("1. Cadastrar novo livro")
    print("2. Listar todos os livros")
    print("3. Buscar livro por titulo")
    print("4. Gerar grafico por genero")
    print("5. Adicionar livros de exemplo")
    print("6. Sair do sistema")
    print("="*50)
    
    # Valida a entrada do usuario
    try:
        opcao = int(input("Escolha uma opcao (1-6): "))
        return opcao
    except ValueError:
        print("Erro: Digite um numero valido!")
        return 0

# Passo 5: Funcao principal do sistema
def main():
    """
    Funcao principal que controla o fluxo do programa
    Implementa o menu e chama as funcoes apropriadas
    """
    print("Bem-vindo ao Sistema de Gerenciamento de Biblioteca!")
    
    while True:
        opcao = exibir_menu()
        
        if opcao == 1:
            cadastrar_livro()
        elif opcao == 2:
            listar_livros()
        elif opcao == 3:
            buscar_livro_por_titulo()
        elif opcao == 4:
            gerar_grafico_por_genero()
        elif opcao == 5:
            adicionar_livros_exemplo()
        elif opcao == 6:
            print("\nObrigado por usar o Sistema de Gerenciamento de Biblioteca!")
            print("Ate logo!")
            break
        else:
            print("Opcao invalida! Escolha uma opcao entre 1 e 6.")
        
        # Pausa para o usuario ver o resultado
        input("\nPressione Enter para continuar...")

# Executa o programa principal
if __name__ == "__main__":
    main()
