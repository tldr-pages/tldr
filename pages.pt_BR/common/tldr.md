# tldr

> Exibe páginas de ajuda simples para ferramentas de linha de comando do projeto tldr-pages.
> Mais informações: <https://github.com/tldr-pages/tldr/blob/main/CLIENT-SPECIFICATION.md#command-line-interface>.

- Imprime a página do tldr para um comando específico (dica: é assim que você chegou aqui!):

`tldr {{comando}}`

- Imprime a página do tldr para um subcomando específico:

`tldr {{comando}}-{{subcomando}}`

- Imprime a página do tldr para um comando para uma [p]lataforma específica:

`tldr -p {{android|linux|osx|sunos|windows}} {{comando}}`

- Atualiza o cache local das páginas do tldr:

`tldr -u`
