# chromium

> Navegador código aberto do Google.
> Mais informações: <https://www.chromium.org/developers/how-tos/run-chromium-with-flags/>.

- Abre um arquivo:

`chromium {{caminho/para/arquivo.html}}`

- Abre uma URL:

`chromium {{exemplo.com}}`

- Abre no modo de navegação anônima (icognito):

`chromium --incognito {{exemplo.com}}`

- Abre em uma nova janela:

`chromium --new-window {{exemplo.com}}`

- Abre no modo app (Sem barra de tarefas, barra de URL, botões, etc.):

`chromium --app='{{https://example.com}}'`

- Usa um servidor proxy:

`chromium --proxy-server="{{socks5://hostname:66}}" {{exemplo.com}}`
