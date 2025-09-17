# Modelo de Machine Learning para Classificacao de Especies de Flores Iris
# Usando TensorFlow para construir, treinar e avaliar o modelo

# Passo 1: Importar Bibliotecas e Carregar Dados
print("=== Passo 1: Importando bibliotecas e carregando dados ===")

import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt

# Carregar conjunto de dados Iris
iris = load_iris()
X = iris.data  # caracteristicas (comprimento e largura das sepalas e petalas)
y = iris.target  # especies (0: setosa, 1: versicolor, 2: virginica)

print(f"Conjunto de dados carregado com sucesso!")
print(f"Formato dos dados: {X.shape}")
print(f"Numero de especies: {len(iris.target_names)}")
print(f"Especies: {iris.target_names}")

# Passo 2: Pre-processamento dos Dados
print("\n=== Passo 2: Pre-processamento dos dados ===")

# Dividir o conjunto de dados em treinamento (80%) e teste (20%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"Dados de treinamento: {X_train.shape[0]} amostras")
print(f"Dados de teste: {X_test.shape[0]} amostras")

# Normalizar os dados usando StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Dados normalizados com sucesso!")

# Passo 3: Construir o Modelo
print("\n=== Passo 3: Construindo o modelo de rede neural ===")

# Criar modelo sequencial usando TensorFlow/Keras
modelo = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(4,)),  # camada oculta
    tf.keras.layers.Dense(8, activation='relu'),  # segunda camada oculta
    tf.keras.layers.Dense(3, activation='softmax')  # camada de saida (3 especies)
])

# Compilar o modelo
modelo.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

print("Modelo construido com sucesso!")
print(modelo.summary())

# Passo 4: Treinar o Modelo
print("\n=== Passo 4: Treinando o modelo ===")

# Treinar o modelo
historico = modelo.fit(
    X_train_scaled, y_train,
    epochs=100,
    batch_size=8,
    validation_split=0.2,
    verbose=2  # Mostra apenas uma linha por epoca (mais limpo para screenshot)
)

print("Modelo treinado com sucesso!")

# Passo 5: Avaliar o Modelo
print("\n=== Passo 5: Avaliando o modelo ===")

# Avaliar o modelo com dados de teste
perda_teste, precisao_teste = modelo.evaluate(X_test_scaled, y_test, verbose=0)
print(f"Precisao no conjunto de teste: {precisao_teste:.4f} ({precisao_teste*100:.2f}%)")
print(f"Perda no conjunto de teste: {perda_teste:.4f}")

# Fazer previsoes nos dados de teste
previsoes = modelo.predict(X_test_scaled)
previsoes_classes = np.argmax(previsoes, axis=1)

# Relatorio de classificacao detalhado
print("\n--- Relatorio de Classificacao ---")
print(classification_report(y_test, previsoes_classes, target_names=iris.target_names))

# Matriz de confusao
print("\n--- Matriz de Confusao ---")
matriz_confusao = confusion_matrix(y_test, previsoes_classes)
print(matriz_confusao)

# Passo 6: Fazer Previsoes
print("\n=== Passo 6: Fazendo previsoes com o modelo treinado ===")

# Exemplos de previsoes
print("\n--- Exemplos de Previsoes ---")
for i in range(5):
    amostra = X_test_scaled[i:i+1]
    previsao = modelo.predict(amostra, verbose=0)
    classe_prevista = np.argmax(previsao)
    probabilidade = np.max(previsao)
    classe_real = y_test[i]
    
    print(f"Amostra {i+1}:")
    print(f"  Caracteristicas originais: {X_test[i]}")
    print(f"  Especie real: {iris.target_names[classe_real]}")
    print(f"  Especie prevista: {iris.target_names[classe_prevista]}")
    print(f"  Probabilidade: {probabilidade:.4f}")
    print(f"  Correto: {'Sim' if classe_prevista == classe_real else 'Nao'}")
    print()

# Funcao para fazer previsao de uma nova amostra
def prever_especie(comprimento_sepala, largura_sepala, comprimento_petala, largura_petala):
    """
    Funcao para prever a especie de uma nova flor iris
    """
    nova_amostra = np.array([[comprimento_sepala, largura_sepala, comprimento_petala, largura_petala]])
    nova_amostra_normalizada = scaler.transform(nova_amostra)
    previsao = modelo.predict(nova_amostra_normalizada, verbose=0)
    classe_prevista = np.argmax(previsao)
    probabilidade = np.max(previsao)
    
    return iris.target_names[classe_prevista], probabilidade

# Exemplo de uso da funcao de previsao
print("--- Exemplo de Previsao para Nova Amostra ---")
especie, prob = prever_especie(5.1, 3.5, 1.4, 0.2)
print(f"Previsao para amostra (5.1, 3.5, 1.4, 0.2): {especie} (probabilidade: {prob:.4f})")

especie, prob = prever_especie(6.5, 3.0, 5.2, 2.0)
print(f"Previsao para amostra (6.5, 3.0, 5.2, 2.0): {especie} (probabilidade: {prob:.4f})")

print("\n=== Aplicacao concluida com sucesso! ===")
