# chromium

> Navegador web de código aberto desenvolvido e mantido principalmente pela Google.
> Mais informações: <https://www.chromium.org/developers/how-tos/run-chromium-with-flags/>.

- Abre uma URL ou arquivo específico:

`chromium {{https://example.com|caminho/para/arquivo.html}}`

- Abre no modo de navegação anônima (incógnito):

`chromium --incognito {{example.com}}`

- Abre em uma nova janela:

`chromium --new-window {{example.com}}`

- Abre no modo aplicativo (sem barra de tarefas, barra de URL, botões, etc.):

`chromium --app={{https://example.com}}`

- Usa um servidor proxy:

`chromium --proxy-server="{{socks5://hostname:66}}" {{example.com}}`

- Abre com um diretório de perfil customizado:

`chromium --user-data-dir={{caminho/para/diretório}}`

- Abre sem validação CORS (útil para testar uma API):

`chromium --user-data-dir={{caminho/para/diretório}} --disable-web-security`

- Abre com uma janela DevTools para cada aba aberta:

`chromium --auto-open-devtools-for-tabs`
