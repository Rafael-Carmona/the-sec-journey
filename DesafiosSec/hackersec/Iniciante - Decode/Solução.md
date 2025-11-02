# Solução do Desafio DECODE

## Comandos usados

### 1) Base64
```bash
echo "U3VwZXIgU2VjcmV0" | base64 -d
# Resultado: Super Secret
```
### 2) Hexadecimal
```bash
echo "73657074656D626572" | xxd -r -p
# Resultado: september
```
### 3) ROT13
```bash
echo "Frperg Zrffntr" | tr 'A-Za-z' 'N-ZA-Mn-za-m'
# Resultado: Secret Message
```
## Montagem da evidência
- Normalize os resultados para letras minúsculas e sem espaços:
  - `Super Secret` -> `supersecret`
  - `september` -> `september`
  - `Secret Message` -> `secretmessage`

- Concatenando em sequência (sem espaços/caracteres especiais):
`supersecretseptembersecretmessage`
