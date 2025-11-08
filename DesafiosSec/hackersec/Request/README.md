> ⚠️ Este desafio foi realizado em ambiente de laboratório (HackerSec). Todos os dados são fictícios.

# 03 - Request (Parameter-based info leak)

**Plataforma:** HackerSec  
**Categoria:** Web (Insecure Direct Object Reference / IDOR / Info Disclosure)  
**Nível:** Iniciante  
**Pontuação:** 18 pontos  
**Status:** Resolvido  

## TL;DR
Dados sensíveis eram acessíveis alterando um parâmetro oculto na URL (ID/param). Resultado encontrado e armazenado aqui com a senha: `hackersec_requestmaster` no repositório público.

## Descrição
Ao analisar um painel web, foi observado que o conteúdo exibido depende de um parâmetro na URL que referencia o perfil/registro do usuário. O controle de acesso não validava se o usuário tinha permissão para visualizar outros perfis, permitindo leitura de dados sensíveis via manipulação de URL.

## Objetivo
Encontrar qual dado é exibido acessando o parâmetro oculto na URL.

## Evidência final (repo)
Senha encontrada: `pass: [REDACTED - discovered via URL parameter]`

## Artefatos
- `solucao.md` — passo a passo técnico e comandos.  
- `imagem/` — screenshot censurada do request/response.  
