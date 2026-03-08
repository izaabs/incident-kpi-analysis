# =====================================================
# PROJETO: Análise de Incidentes Operacionais
# Objetivo:
# - Gerar uma base de dados simulada
# - Calcular KPIs operacionais
# - Identificar gargalos e padrões
# =====================================================

import pandas as pd
import numpy as np

# -----------------------------------------------------
# 1. GERANDO DADOS SIMULADOS
# -----------------------------------------------------

# define uma "seed" para garantir que os números aleatórios sejam sempre os mesmos quando o código rodar novamente.
np.random.seed(42) 

# criando um dicionário com colunas simuladas, cada coluna representa um atributo do incidente
dados = {
    "canal": np.random.choice(["App Mobile", "Web", "API Parceiros"], 60), # np.random.choice escolhe valores aleatórios de uma lista
    "tipo_incidente": np.random.choice(["Erro Login", "Timeout API", "Lentidão", "Erro Pagamento"], 60),
    "prioridade": np.random.choice(["Alta", "Média", "Baixa"], 60),
    "tempo_resolucao_horas": np.random.uniform(0.5, 8, 60).round(2), # np.random.uniform gera números decimais aleatórios entre 0.5 e 8 horas
    "sla_horas": np.random.choice([2,4,6], 60),
    "clientes_afetados": np.random.randint(10,2000,60) # np.random.randint gera números inteiros aleatórios.
}

df = pd.DataFrame(dados) # transforma o dicionário em um DataFrame

# mostra as primeiras linhas da base para inspeção inicial
print("\nBase de dados: ")
print(df.head())

# -----------------------------------------------------
# 2. CÁLCULO DE KPIs OPERACIONAIS
# -----------------------------------------------------

print("\n--- KPIs ---\n")

# KPI 1: Volume total de incidentes
print("Total de incidentes:", len(df))  # len(df) conta o número de linhas do DataFrame

# KPI 2: Tempo médio de resolução (MTTR)
print(
    "Tempo médio de resolução: ",
    round(df["tempo_resolucao_horas"].mean(), 2), # .mean() calcula a média da coluna e round(...,2) arredonda para duas casas decimais
    "horas"
    )

# KPI 3: Percentual de SLA cumprido
# criamos uma nova coluna chamada "sla_cumprido"
df["sla_cumprido"] = df["tempo_resolucao_horas"] <= df["sla_horas"] # a comparação verifica se o tempo de resolução foi menor ou igual ao SLA

# true = 1 e false = 0, calcular a média dessa coluna retorna o percentual de sucesso
print(
    "Percentual do SLA cumprido: ",
    round(df["sla_cumprido"].mean() * 100, 2),
    "%"
)

# KPI 4: Total de clientes afetados
print(
    "Total de clientes afetados: ",
    df["clientes_afetados"].sum() # .sum() soma todos os valores da coluna
)

# -----------------------------------------------------
# 3. ANÁLISE DE PADRÕES
# -----------------------------------------------------

# Identificar quais canais apresentam mais incidentes
print("\nIncidentes por canal: ")
print(df["canal"].value_counts())

# Identificar quais tipos de incidentes são mais frequentes
print("\nIncidentes por tipo: ")
print(df["tipo_incidente"].value_counts())

# Calcular o tempo médio de resolução por canal
print("\nTempo médio de resolução por canal: ")
print(df.groupby("canal")["tempo_resolucao_horas"].mean()) # groupby agrupa os dados pela coluna especificada

# Identificar quais incidentes impactam mais clientes
print("\nClientes afetados por tipo de incidentes: ")
print(df.groupby("tipo_incidente")["clientes_afetados"].sum())

# -----------------------------------------------------
# 4. IDENTIFICAÇÃO DE GARGALOS
# -----------------------------------------------------

print("\n--- Possíveis Gargalos ---\n")

# Canal com maior tempo médio de resolução
gargalo_canal = df.groupby("canal")["tempo_resolucao_horas"].mean().idxmax() # idxmax retorna o índice com maior valor
print("Canal com maior tempo médio de resolução: ", gargalo_canal)

# Tipo de incidente mais recorrente
tipo_mais_comum_inc = df["tipo_incidente"].value_counts().idxmax()
print("Tipo de incidente mais recorrente: ", tipo_mais_comum_inc)

# Tipo de incidente com maior impacto em clientes
maior_impacto_inc = df.groupby("tipo_incidente")["clientes_afetados"].sum().idxmax()
print("Tipo de incidente com maior impacto em clientes: ", maior_impacto_inc)

# -----------------------------------------------------
# FIM DA ANÁLISE
# -----------------------------------------------------

print("\nAnálise concluída com sucesso.")