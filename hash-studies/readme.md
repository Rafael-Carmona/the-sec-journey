# Análise do hashe SHA256
## 💭 O que é SHA-256?
### SHA-256 é um algoritmo de hash criptográfico que transforma qualquer entrada (texto, arquivo, etc.) numa sequência fixa de 256 bits. É como uma impressão digital única para o seu conteúdo
## 💻+ Sobre este mini-projeto 
### Nesse mini-sistema, eu construi um mecanismo onde você poderá tranformar textos em hashes
## 🧑‍💻 Como funciona o programa?
Para poder usar esse código, é só rodar o **script Python** no seu ambiente de desenvolvimento. O programa vai te o menu com 3 opções
1. **Gerar hash de um texto**
- Nesta opção, será pedido pra que digite um texto qualquer e vai gerar o hash SHA256 desse texto
2. **Comparar dois textos**
- Nesta opção, será pedido pra que digite texto 1 e logo em seguida o texto 2 e vai ser comparado dois textos e ver se têm o mesmo hash
3. **Sair**
- Nessa opção é apenas pra sair do menu

## 📸 Print do programa

Aqui está um exemplo de como fica o menu no VScode:

![Menu do programa](code.jpng)

## ⚙️ Função principal

Aqui está a função que gera o hash SHA256 de um texto:

```
import hashlib

def gerar_sha256(texto):
    return hashlib.sha256(texto.encode()).hexdigest()
```


