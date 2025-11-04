# Solução do Desafio — LoginPage

## Resumo
Encontrei credenciais codificadas no código-fonte da página e as decodifiquei usando o terminal. Resultado final: **admin:h4ck3rs3c**.

## Passo a passo

1. Acessei a página do desafio (URL do desafio).
2. Abri as ferramentas de desenvolvedor do navegador (botão direito → **Inspecionar** ou atalho **F12** / **Ctrl+Shift+I**).
3. No painel **Elements** (ou **Sources**), procurei por `<script>` 
4. Encontrei no código:
<pre style="background:
#2b2828ff; color:#cccccc; padding:10px; border-radius:5px; font-family: monospace;">
<span style="color:#852b9e;">const</span> <span style="color:#569cd6;">encodedUser</span> = <span style="color:#d96416;">"YWRtaW4=";</span>
<span style="color:#852b9e;">const</span> <span style="color:#569cd6;">encodedPass</span> = <span style="color:#d96416;">"aDRjazNyczNj";</span></pre>
### Essas credenciais estão criptografadas então pra quebrar eu usei no terminal bash esse código:
<pre style="background:black; color:#cccccc; padding:10px; border-radius:5px; font-family: monospace;">
<span style="color:#569cd6;">echo</span> <span style="color:#d69d85;">"YWRtaW4="</span> <span style="color:#569cd6;">|</span> <span style="color:#6a9955;">base64</span> <span style="color:#6a9955;">-d</span>
<span style="color:#569cd6;">echo</span> <span style="color:#d69d85;">"aDRjazNyczNj"</span> <span style="color:#569cd6;">|</span> <span style="color:#6a9955;">base64</span> <span style="color:#6a9955;">-d</span>
</pre>

- Então, eu obtive o resultado pedido pelo desafio: **admin:h4ck3rs3c**