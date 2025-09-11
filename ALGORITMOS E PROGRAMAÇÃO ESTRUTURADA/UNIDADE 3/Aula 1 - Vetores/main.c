#include <stdio.h>
#include <locale.h>

int main() {
    // Configura a localizacao para portugues brasileiro
    setlocale(LC_ALL, "Portuguese");
    
    // Declaracao do vetor de tamanho 5 para armazenar numeros inteiros
    int vendas[5];
    int soma = 0;
    int i;
    
    // Cabecalho do programa
    printf("=== SISTEMA DE ANALISE DE VENDAS DIARIAS ===\n");
    printf("Sistema para armazenar e analisar dados de vendas de uma pequena loja\n\n");
    
    // Solicita ao usuario que insira 5 valores inteiros
    printf("Por favor, insira a quantidade de vendas realizadas em 5 dias:\n\n");
    
    for (i = 0; i < 5; i++) {
        printf("Digite a quantidade de vendas do dia %d: ", i + 1);
        scanf("%d", &vendas[i]);
        
        // Calcula a soma dos valores conforme sao inseridos
        soma += vendas[i];
    }
    
    // Exibe uma linha separadora
    printf("\n" "========================================\n");
    printf("RELATORIO DE VENDAS\n");
    printf("========================================\n\n");
    
    // Exibe todos os elementos do vetor, um por linha
    printf("Quantidade de vendas por dia:\n");
    for (i = 0; i < 5; i++) {
        printf("Dia %d: %d vendas\n", i + 1, vendas[i]);
    }
    
    // Exibe a soma total dos valores
    printf("\n" "========================================\n");
    printf("Total geral de vendas no periodo: %d\n", soma);
    printf("========================================\n");
    
    return 0;
}