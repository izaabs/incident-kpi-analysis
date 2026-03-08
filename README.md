# 📊 Incident KPI Analysis with Python

Projeto de análise exploratória de dados focado em incidentes operacionais, utilizando Python e bibliotecas de análise de dados para calcular indicadores de desempenho (KPIs) e identificar gargalos no sistema.

---

## 🎯 Objetivo

O objetivo deste projeto é simular uma base de incidentes operacionais e realizar uma análise para:

- Calcular indicadores-chave de desempenho (KPIs)
- Identificar gargalos operacionais
- Encontrar padrões de incidentes
- Avaliar impacto em clientes
- Explorar métricas importantes de confiabilidade

---

## 📂 Estrutura de Dados

A base de dados simulada contém as seguintes colunas:

| Coluna | Descrição |
|------|------|
| canal | Canal onde o incidente ocorreu (App Mobile, Web, API Parceiros) |
| tipo_incidente | Categoria do incidente |
| prioridade | Nível de prioridade do incidente |
| tempo_resolucao_horas | Tempo necessário para resolver o incidente |
| sla_horas | Tempo máximo permitido pelo SLA |
| clientes_afetados | Quantidade de clientes impactados |

Os dados são gerados de forma simulada utilizando Python.

---

## 📈 KPIs Calculados

Durante a análise foram calculados os seguintes indicadores:

### Volume total de incidentes
Número total de incidentes registrados.

### Tempo médio de resolução (MTTR)
Tempo médio necessário para resolver incidentes.

### Percentual de SLA cumprido
Percentual de incidentes resolvidos dentro do tempo definido no SLA.

### Impacto em clientes
Total de clientes afetados pelos incidentes.

---

## 🔎 Análises Realizadas

O projeto também explora padrões nos dados:

- Incidentes por canal
- Incidentes por tipo
- Tempo médio de resolução por canal
- Impacto de incidentes em clientes

Essas análises ajudam a identificar possíveis **gargalos operacionais**.

---

## 🚨 Identificação de Gargalos

Com base nos dados analisados, o projeto identifica:

- Canal com maior tempo médio de resolução
- Tipo de incidente mais recorrente
- Tipo de incidente com maior impacto em clientes

Essas informações podem auxiliar na priorização de melhorias operacionais.

---

## 🛠 Tecnologias Utilizadas

- Python
- Pandas
- NumPy
- Git
- GitHub

---

## 👩‍💻 Autor

Projeto desenvolvido para fins acadêmicos e prática em estruturação e análise de dados.
