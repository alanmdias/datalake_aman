# 00 — Contexto do Projeto

## A empresa

**AMAN** é uma fintech em fase inicial focada em crédito para o mercado de Real Estate.

O principal objetivo da empresa é construir um **motor proprietário de análise de crédito** para compra de carteiras de recebíveis de loteamentos.

## O ativo central de dados

A AMAN recebeu acesso a uma base histórica da **San Marino** — ERP imobiliário que gerencia loteamentos. A base contém aproximadamente **35 anos de dados operacionais** (clientes, lotes, vendas, cobranças, financeiro, inadimplência, entre outros).

Essa base é o principal ativo de dados da empresa e a razão de existir deste projeto de engenharia de dados.

## Problema atual

A AMAN não possui infraestrutura própria de dados. O acesso à base da San Marino ocorre via VPN, diretamente no banco PostgreSQL da San Marino. Isso gera:

- Dependência total da infraestrutura da San Marino
- Sem histórico próprio dos dados
- Sem capacidade de análise estruturada
- Sem base para modelos de crédito

## Objetivo do projeto

Criar a primeira arquitetura de dados da AMAN, com:

- Independência da infraestrutura da San Marino
- Armazenamento próprio dos dados
- Atualização automatizada
- Documentação técnica
- Exploração via Claude
- Preparação para futuras análises e modelos de crédito

## Repositório

- GitHub: https://github.com/alanmdias/datalake_aman
- Criado em junho de 2026

## Pessoas envolvidas

- **Alan Dias** (alandias.m@gmail.com) — responsável técnico pelo projeto

## Tecnologias em uso (Etapa 1)

- **Python 3.10** com pandas, psycopg2, openpyxl
- **PostgreSQL** — banco de origem (San Marino)
- **Google Drive API v3** — destino intermediário dos arquivos
- **OAuth2** — autenticação Google via conta do Alan
