# snakefmt

> Formata arquivos Snakemake.
> Mais informações: <https://github.com/snakemake/snakefmt>.

- Formata um Snakefile específico:

`snakefmt {{caminho/para/snakefile}}`

- Formata todos os Snakefiles recursivamente em uma pasta específica:

`snakefmt {{caminho/para/diretorio}}`

- Formata um arquivo usando um arquivo de configuração específico:

`snakefmt --config {{caminho/para/config.toml}} {{caminho/para/snakefile}}`

- Formata um arquivo usando um comprimento máximo de linha específico:

`snakefmt --line-length {{100}} {{caminho/para/snakefile}}`

- Exibe às mudanças que seriam realizadas sem realiza-las:

`snakefmt --diff {{caminho/para/snakefile}}`
