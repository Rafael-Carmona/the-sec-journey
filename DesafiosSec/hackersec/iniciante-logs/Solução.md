# Solução do Desafio Logs

## Resolvendo o Desafio

1. Abri o arquivo de logs e observei o padrão de cada linha, que segue o formato:
```bash
<IP> - - [timestamp] "MÉTODO HTTP /CAMINHO HTTP" CÓDIGO_DE_STATUS
```

2. Listei os IPs presentes e observei quais tentavam acessar caminhos incomuns ou sensíveis.

3. Identifiquei requisições com **padrões suspeitos**, como:

- Uso de `../` tentando acessar arquivos do sistema.
- Acesso direto a arquivos do sistema, como `/etc/passwd`, `/etc/shadow`.

Analisando os logs, o IP **45.225.86.252** se destacou por tentar acessar vários arquivos do sistema desse estilo:

```bash
/../../../../etc/passwd
/../../../etc/shadow
/etc/passwd
/../../../etc/security/passwd
```
Essas requisições mostram claramente uma tentativa de sair do diretório raiz do site e acessar arquivos sensíveis do servidor.

✅ **IP do atacante:** `45.225.86.252`

---

## Tipo de Ataque

O padrão de requisições com `../` ou acesso direto a arquivos do sistema caracteriza um **Directory Traversal**

✅ **Tipo de ataque:** `Directory Traversal`

---

## Entrada que o Atacante Tentou Acessar

O arquivo mais clássico e sensível que o atacante tentou acessar foi o **`/etc/passwd`**, que contém informações sobre os usuários do sistema. 

✅ **Entrada acessada:** `/../../../../etc/passwd`

---

## Conclusão

A análise dos logs permitiu identificar o atacante, o tipo de ataque e a entrada que ele tentou acessar. Esse tipo de investigação é fundamental para reforçar a segurança de servidores web, detectando padrões maliciosos e bloqueando acessos indevidos.

