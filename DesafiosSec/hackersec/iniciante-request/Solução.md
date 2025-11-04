# Solução do Desafio — LoginPage

## Resumo
Encontrei uma senha secreta através de um parâmetro oculto na URL: **hackersec_requestmaster**.

## Passo a passo

1. Acessei a página do desafio (URL do desafio).
2. Reparei na URL da pagina e percebi uma brecha pra testar alguns paramentros, a brecha era **profile=guest** que estava escrito no final da Url
3. Alterei o que tava escrito: gest, para admin, quando mandei a requisição:
4. Apareceu uma pagina que dizia:
<pre>Bem-vindo Admin! A senha secreta é: hackersec_requestmaster</pre>