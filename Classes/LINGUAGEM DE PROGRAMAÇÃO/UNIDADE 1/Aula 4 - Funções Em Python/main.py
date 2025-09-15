# Sistema de Gestao de Notas de Alunos
# Desenvolvido para gerenciar notas, calcular medias e determinar situacao dos alunos

def adicionar_notas():
    """
    Funcao para adicionar notas do aluno.
    Permite ao usuario inserir multiplas notas que sao armazenadas em uma lista.
    Retorna uma lista com todas as notas inseridas.
    """
    notas = []
    print("=== CADASTRO DE NOTAS ===")
    print("Digite as notas do aluno (digite -1 para finalizar)")
    
    while True:
        try:
            # Solicita entrada da nota
            nota = float(input("Digite a nota: "))
            
            # Condicao para parar a insercao de notas
            if nota == -1:
                break
            
            # Validacao da nota (deve estar entre 0 e 10)
            if nota < 0 or nota > 10:
                print("Erro: A nota deve estar entre 0 e 10. Tente novamente.")
                continue
            
            # Adiciona a nota valida na lista
            notas.append(nota)
            print(f"Nota {nota} adicionada com sucesso!")
            
        except ValueError:
            print("Erro: Digite um numero valido.")
    
    return notas

def calcular_media(notas):
    """
    Funcao para calcular a media das notas.
    Recebe uma lista de notas e retorna a media aritmetica.
    """
    if len(notas) == 0:
        return 0
    
    # Calcula a soma de todas as notas
    soma = sum(notas)
    
    # Calcula a media dividindo a soma pelo numero de notas
    media = soma / len(notas)
    
    return media

def determinar_situacao(media):
    """
    Funcao para determinar a situacao do aluno baseada na media.
    Se media >= 7: Aprovado
    Se media < 7: Reprovado
    """
    if media >= 7:
        return "APROVADO"
    else:
        return "REPROVADO"

def exibir_relatorio(notas, media, situacao):
    """
    Funcao para exibir o relatorio final com todas as informacoes do aluno.
    Mostra as notas inseridas, a media calculada e a situacao final.
    """
    print("\n" + "="*50)
    print("           RELATORIO FINAL DO ALUNO")
    print("="*50)
    
    # Exibe todas as notas inseridas
    print(f"Notas inseridas: {notas}")
    print(f"Quantidade de notas: {len(notas)}")
    
    # Exibe a media com 2 casas decimais
    print(f"Media das notas: {media:.2f}")
    
    # Exibe a situacao do aluno
    print(f"Situacao: {situacao}")
    
    # Adiciona uma mensagem personalizada baseada na situacao
    if situacao == "APROVADO":
        print("Parabens! Voce foi aprovado!")
    else:
        print("Infelizmente voce foi reprovado. Continue estudando!")
    
    print("="*50)

def main():
    """
    Funcao principal que coordena todo o sistema.
    Chama todas as outras funcoes na ordem correta.
    """
    print("Sistema de Gestao de Notas de Alunos")
    print("Bem-vindo ao sistema!")
    
    # Estrutura de repeticao para permitir processar multiplos alunos
    while True:
        try:
            # Cadastro de notas
            notas_aluno = adicionar_notas()
            
            # Verifica se pelo menos uma nota foi inserida
            if len(notas_aluno) == 0:
                print("Nenhuma nota foi inserida. Encerrando o sistema.")
                break
            
            # Calcula a media das notas
            media_aluno = calcular_media(notas_aluno)
            
            # Determina a situacao do aluno
            situacao_aluno = determinar_situacao(media_aluno)
            
            # Exibe o relatorio final
            exibir_relatorio(notas_aluno, media_aluno, situacao_aluno)
            
            # Pergunta se o usuario quer processar outro aluno
            continuar = input("\nDeseja processar outro aluno? (s/n): ").lower()
            if continuar != 's':
                break
                
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            break
    
    print("Obrigado por usar o Sistema de Gestao de Notas!")

# Executa o programa principal apenas se este arquivo for executado diretamente
if __name__ == "__main__":
    main()
