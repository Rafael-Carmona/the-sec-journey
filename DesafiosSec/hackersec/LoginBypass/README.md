> ⚠️ Este desafio foi realizado em ambiente de laboratório (HackerSec). Todos os dados são fictícios.

# Login by pass

**Plataforma:** HackerSec  
**Categoria:** Web (Auth Bypass / Info Disclosure)  
**Nível:** Intermediário  
**Pontuação:** 20 pontos  
**Status:** Resolvido  

## TL;DR
O painel restrito libera acesso quando um cookie ou header específico é fornecido. Exploitei o bypass definindo o cookie/header correto e coletei a flag: `hackersec-loginbypass-dh49a`.

## Descrição
O backend confia na presença de um cookie ou header para liberar o acesso ao painel administrativo. Ao testar valores comuns e headers customizados, foi possível bypassar a autenticação e recuperar a flag presente na página administrativa.

## Objetivo
Obter acesso ao painel restrito e coletar a flag.

## Evidência final (repo)
Flag encontrada: `hackersec-loginbypass-dh49a`

## Artefatos
- `solucao.md` — passo a passo técnico e comandos.  


