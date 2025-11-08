# Solução do Desafio — Login Bypass

## Resumo
Acessei o painel do desafio pela vulnerabilidade de autenticação baseada em cookie.

## Passo a passo

1. Abri a página do desafio no navegador (a URL do desafo).
2. Pressionei **F12** → **Application**.
3. No menu lateral: **Storage → Cookies → https://capturetheflag.com.br** 
4. Cliquei no botão **+** (ou botão direito → **Add**).
   - **Name**: `auth`
   - **Value**: `admin`
   - **Path**: `/`
   - Pressionei **Enter** para salvar.
5. Recarreguei a página (F5).
6. Copiei a flag exibida no painel: `hackersec-loginbypass-dh49a`.

---

## Uma outra opção que pode ser feita é
- **Console (one-liner)**:
```javascript
document.cookie = "auth=admin; path=/"; location.reload();
``` 
e com isso ir testando outras variedades

### Achamos a flag: **hackersec-traversal-a913f**