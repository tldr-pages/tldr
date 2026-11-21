# dot_clean

> Mescla ._* arquivos com arquivos nativos correspondentes.
> Mais informações: <https://keith.github.io/xcode-man-pages/dot_clean.1.html>.

- Mescla todos os `._*` arquivos recursivamente:

`dot_clean {{caminho/para/diretorio}}`

- Não mescla recursivamente todos `._*` em um diretório (flat merge):

`dot_clean -f {{caminho/para/diretorio}}`

- Mescla e exclui todos os arquivos `._*`:

`dot_clean -m {{caminho/para/diretorio}}`

- Somente exclui arquivos `._*` se houver um arquivo nativo correspondente:

`dot_clean -n {{caminho/para/diretorio}}`

- Segue os links simbólicos:

`dot_clean -s {{caminho/para/diretorio}}`

- Imprime saída verbosa:

`dot_clean -v {{caminho/para/diretorio}}`
