#include <stdio.h>
#include <locale.h>

// Funcao para calcular o salario bruto
float calcular_salario_bruto(float valor_hora, float horas_trabalhadas) {
    return valor_hora * horas_trabalhadas;
}

// Funcao para calcular o desconto de 9%
float calcular_desconto(float salario_bruto) {
    return salario_bruto * 0.09;
}

// Funcao para calcular o salario liquido
float calcular_salario_liquido(float salario_bruto, float desconto) {
    return salario_bruto - desconto;
}

int main() {
    // Configura a localizacao para exibir caracteres especiais em portugues
    setlocale(LC_ALL, "");
    
    // Declaracao das variaveis
    float valor_hora, horas_trabalhadas;
    float salario_bruto, desconto, salario_liquido;
    
    // Solicitacao dos dados ao usuario
    printf("=== CALCULADORA DE SALARIO ===\n\n");
    printf("Digite o valor da sua hora de trabalho (R$): ");
    scanf("%f", &valor_hora);
    
    printf("Digite a quantidade de horas trabalhadas no mes: ");
    scanf("%f", &horas_trabalhadas);
    
    // Calculo do salario bruto usando a funcao
    salario_bruto = calcular_salario_bruto(valor_hora, horas_trabalhadas);
    
    // Calculo do desconto usando a funcao
    desconto = calcular_desconto(salario_bruto);
    
    // Calculo do salario liquido usando a funcao
    salario_liquido = calcular_salario_liquido(salario_bruto, desconto);
    
    // Exibicao dos resultados
    printf("\n=== RESULTADOS ===\n");
    printf("Salario Bruto: R$ %.2f\n", salario_bruto);
    printf("Desconto (9%%): R$ %.2f\n", desconto);
    printf("Salario Liquido: R$ %.2f\n", salario_liquido);
    
    return 0;
}