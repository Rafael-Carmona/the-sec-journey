> ⚠️ Este desafio foi realizado em ambiente de laboratório (HackerSec). Todos os dados são fictícios.

# IDOR

**Plataforma:** HackerSec  
**Categoria:** Web (IDOR / Insecure Direct Object Reference)  
**Nível:** Intermediário  
**Pontuação:** 18 pontos  
**Status:** Resolvido  

## TL;DR
Dados sensíveis expostos por IDOR: ao manipular um ID numérico na URL foi possível acessar o perfil privilegiado e extrair a API key/token. Token coletado: `hackersec_idoraccess`.

## Descrição
A aplicação carrega dados via um identificador numérico na URL e não valida se o usuário autenticado tem permissão para ver aquele recurso. Foi possível enumerar IDs e acessar dados de outro usuário privilegiado.

## Objetivo
Encontrar no painel a API KEY ou token sensível do perfil privilegiado.

## Evidência final (repo)
Token encontrado: `hackersec_idoraccess`

## Artefatos
- `solucao.md` — passo a passo técnico e comandos (reproduzível).  
- `scripts/` — script de enumeração de IDs (opcional).  
- `imagem/` — Evidencia visual


