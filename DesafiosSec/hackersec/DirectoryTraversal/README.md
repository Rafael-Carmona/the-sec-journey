> ⚠️ Este desafio foi realizado em ambiente de laboratório (HackerSec). Todos os dados são fictícios.

# Directory Traversal

**Plataforma:** HackerSec  
**Categoria:** Web (Directory Traversal / Local File Read)  
**Nível:** Intermediário  
**Pontuação:** 22 pontos  
**Status:** Resolvido  

## TL;DR
A funcionalidade de visualização de arquivos é vulnerável a Directory Traversal. Explorando `../` na entrada, acessei arquivo sensível e recuperei a flag: `hackersec-traversal-a913f`.

## Descrição
O sistema permite visualizar arquivos com base num parâmetro de caminho. Sem sanitização/normalização adequada, é possível subir diretórios usando `../` e ler arquivos fora da área permitida.

## Objetivo
Acessar arquivo sensível e extrair a flag embutida no conteúdo.

## Evidência final (repo)
Flag encontrada: `hackersec-traversal-a913f`

## Artefatos
- `solucao.md` — passo a passo técnico e comandos.  

