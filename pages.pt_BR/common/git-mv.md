# git mv

> Move ou renomeia arquivos e atualiza o index do Git.
> Mais informações: <https://git-scm.com/docs/git-mv>.

- Move arquivos dentro de um repositório e adiciona no próximo commit:

`git mv {{caminho/para/arquivo}} {{novo/caminho}}`

- Renomeia um arquivo e adiciona a renomeação no próximo commit:

`git mv {{nome_do_arquivo}} {{novo_nome}}`

- Sobrescreve o arquivo no caminho alvo se ele já existir:

`git mv {{[-f|--force]}} {{arquivo}} {{alvo}}`
