# chromium

> Navegador código aberto desenvolvido principalmente e mantido pela Google.
> Mais informações: <https://www.chromium.org/developers/how-tos/run-chromium-with-flags/>.

- Abre uma URL ou arquivo específico:

`chromium {{https://exemplo.com|caminho/para/arquivo.html}}`

- Abre no modo de navegação anônima (incógnito):

`chromium --incognito {{exemplo.com}}`

- Abre em uma nova janela:

`chromium --new-window {{exemplo.com}}`

- Abre no modo aplicativo (Sem barra de tarefas, barra de URL, botões, etc.):

`chromium --app {{https://exemplo.com}}`

- Usa um servidor proxy:

`chromium --proxy-server="{{socks5://hostname:66}}" {{exemplo.com}}`

- Abre com um diretório de perfil customizado:

`chromium --user-data-dir {{caminho/para/arquivo}}`

- Abre sem validação CORS (útil para testar uma API):

`chromium --user-data-dir {{caminho/para/arquivo}} --disable-web-security`

- Abre com uma janela DevTools para cada aba aberta:

`chromium --auto-open-devtools-for-tabs`
