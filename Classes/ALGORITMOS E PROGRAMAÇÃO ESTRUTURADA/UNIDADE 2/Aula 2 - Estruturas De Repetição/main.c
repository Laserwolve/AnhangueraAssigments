#include <stdio.h>

int main() {
    int numero;
    int soma = 0;
    int resultado_scanf;
    
    printf("=== CALCULADORA DE SOMA ===\n");
    printf("Digite numeros inteiros para somar.\n");
    printf("Digite 0 (zero) para encerrar o programa.\n\n");
    
    // Loop while com teste da condicao no inicio
    printf("Digite um numero inteiro: ");
    resultado_scanf = scanf("%d", &numero);
    
    // Validacao da entrada inicial
    while (resultado_scanf != 1) {
        // Limpa o buffer de entrada
        while (getchar() != '\n');
        printf("Entrada invalida! Digite apenas numeros inteiros.\n");
        printf("Digite um numero inteiro: ");
        resultado_scanf = scanf("%d", &numero);
    }
    
    while (numero != 0) {
        soma += numero;
        printf("Soma atual: %d\n", soma);
        printf("Digite um numero inteiro: ");
        resultado_scanf = scanf("%d", &numero);
        
        // Se a entrada nao for um inteiro valido, nao adiciona nada e nao mostra a soma
        while (resultado_scanf != 1) {
            // Limpa o buffer de entrada
            while (getchar() != '\n');
            printf("Entrada invalida! Digite apenas numeros inteiros.\n");
            printf("Digite um numero inteiro: ");
            resultado_scanf = scanf("%d", &numero);
        }
    }
    
    printf("\n=== RESULTADO FINAL ===\n");
    printf("A soma de todos os numeros inseridos e: %d\n", soma);
    printf("Programa encerrado.\n");
    
    return 0;
}