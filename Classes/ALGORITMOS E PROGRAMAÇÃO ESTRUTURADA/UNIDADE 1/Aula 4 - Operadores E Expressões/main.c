
#include <stdio.h>

int main() {
    int num1, num2, num3;
    int result;
    printf("Digite o primeiro numero inteiro: ");
    result = scanf("%d", &num1);
    if (result != 1) {
        printf("Entrada invalida! Por favor, insira um numero inteiro.\n");
        return 1;
    }

    printf("Digite o segundo numero inteiro: ");
    result = scanf("%d", &num2);
    if (result != 1) {
        printf("Entrada invalida! Por favor, insira um numero inteiro.\n");
        return 1;
    }

    printf("Digite o terceiro numero inteiro: ");
    result = scanf("%d", &num3);
    if (result != 1) {
        printf("Entrada invalida! Por favor, insira um numero inteiro.\n");
        return 1;
    }

    // Operacoes aritmeticas
    int soma = num1 + num2 + num3;
    int subtracao = num1 - num2 - num3;
    int multiplicacao = num1 * num2 * num3;
    if (num2 == 0 || num3 == 0) {
        printf("Divisao: ERRO (divisao por zero)\n");
    } else {
        float divisao = (float)num1 / num2 / num3;
        printf("Divisao: %.2f\n", divisao);
    }

    printf("Soma: %d\n", soma);
    printf("Subtracao: %d\n", subtracao);
    printf("Multiplicacao: %d\n", multiplicacao);

    // Operadores relacionais
    if (num1 > num2) {
        printf("O primeiro numero (%d) e maior que o segundo (%d).\n", num1, num2);
    } else {
        printf("O primeiro numero (%d) NAO e maior que o segundo (%d).\n", num1, num2);
    }

    if (num2 < num3) {
        printf("O segundo numero (%d) e menor que o terceiro (%d).\n", num2, num3);
    } else {
        printf("O segundo numero (%d) NAO e menor que o terceiro (%d).\n", num2, num3);
    }

    // Operadores logicos
    if (num1 > 0 && num2 % 2 == 0) {
        printf("O primeiro numero e positivo E o segundo numero e par.\n");
    } else {
        printf("A condicao de numero positivo e par nao foi satisfeita.\n");
    }

    return 0;
}
