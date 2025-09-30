# diff

> Compara diretórios e arquivos.
> Mais informações: <https://manned.org/diff>.

- Compara arquivos (mostra as mudanças necessárias para transformar `arquivo_antigo` em `arquivo_novo`):

`diff {{arquivo_antigo}} {{arquivo_novo}}`

- Compara arquivos, ignorando espaço:

`diff {{[-w|--ignore-all-space]}} {{arquivo_antigo}} {{arquivo_novo}}`

- Compara arquivos, mostrando diferenças lado a lado:

`diff {{[-y|--side-by-side]}} {{arquivo_antigo}} {{arquivo_novo}}`

- Compara arquivos, mostrando as diferenças de forma padronizada como feito por `git diff`:

`diff {{[-u|--unified]}} {{arquivo_antigo}} {{arquivo_novo}}`

- Compara diretórios recursivamente (mostra nomes de diretórios e arquivos diferentes assim como mudanças nos arquivos):

`diff {{[-r|--recursive]}} {{arquivo_antigo}} {{arquivo_novo}}`

- Compara diretórios, mostrando apenas os nomes dos arquivos diferentes:

`diff {{[-r|--recursive]}} {{[-q|--brief]}} {{arquivo_antigo}} {{arquivo_novo}}`

- Cria um arquivo patch para o Git a partir das diferenças entre dois arquivos, tratando arquivos ausentes como vazios:

`diff {{[-a|--text]}} {{[-u|--unified]}} {{[-N|--new-file]}} {{arquivo_antigo}} {{arquivo_novo}} > {{diferenca.patch}}`

- Compara arquivos, mostra a saída em cores e tenta fortemente encontrar um conjunto menor de alterações:

`diff {{[-d|--minimal]}} --color=always {{arquivo_antigo}} {{arquivo_novo}}`
