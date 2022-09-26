# firefox

> Um browser livre e de código aberto.
> Mais informações: <https://developer.mozilla.org/en-US/docs/Mozilla/Command_Line_Options>.

- Inicie o Firefox e abra uma página web:

`firefox {{https://www.duckduckgo.com}}`

- Abra uma nova janela:

`firefox --new-window {{https://www.duckduckgo.com}}`

- Abra uma janela privativa (incognito):

`firefox --private-window`

- Pesquise por "wikipedia" usando a engine de busca padrão:

`firefox --search "{{wikipedia}}"`

- Inicie o Firefox no modo seguro, com todas as extensões desativadas:

`firefox --safe-mode`

- Tire uma screenshot de uma página web no modo headless:

`firefox --headless --screenshot {{caminho/para/arquivo_de_saida.png}} {{https://exemplo.com/}}`

- Use um perfil específico para permitir que múltiplas instâncias separadas do Firefox rodem ao mesmo tempo:

`firefox --profile {{caminho/para/diretório}} {{https://example.com/}}`

- Configure o Firefox como o navegador padrão:

`firefox --setDefaultBrowser`
