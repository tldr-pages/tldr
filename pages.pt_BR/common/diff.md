# diff

> Compara diretórios e arquivos.
> Mais informações: <https://man7.org/linux/man-pages/man1/diff.1.html>.

- Compara arquivos (mostra as mudanças necessárias para transformar `arquivo_antigo` em `arquivo_novo`):

`diff {{arquivo_antigo}} {{arquivo_novo}}`

- Compara arquivos, ignorando espaço:

`diff --ignore-all-space {{arquivo_antigo}} {{arquivo_novo}}`

- Compara arquivos, mostrando diferenças lado a lado

`diff --side-by-side {{arquivo_antigo}} {{arquivo_novo}}`

- Compara arquivos, mostrando as diferenças de forma padronizada como feito por `git diff`:

`diff --unified {{arquivo_antigo}} {{arquivo_novo}}`

- Compara diretórios recursivamente, mostrando nomes de diretórios e arquivos diferentes e listando as diferenças entre os arquivos:

`diff --recursive {{arquivo_antigo}} {{arquivo_novo}}`

- Compara diretórios, mostrando apenas os nomes dos arquivos diferentes:

`diff --recursive --brief {{arquivo_antigo}} {{arquivo_novo}}`

- Cria um arquivo patch para o Git a partir das diferenças entre dois arquivos, tratando arquivos ausentes como vazios:

`diff --text --unified --new-file {{arquivo_antigo}} {{arquivo_novo}} > {{diferenca.patch}}`
