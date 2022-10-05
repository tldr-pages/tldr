# snakefmt

> Formata arquivos Snakemake. Mais informações: <https://github.com/snakemake/snakefmt>.

- Formata um Snakefile específico:

`snakefmt {{path/to/snakefile}}`

- Formata todos os Snakefiles recursivamente em uma pasta específica:

`snakefmt {{path/to/directory}}`

- Formata um arquivo usando um arquivo de configuração específico:

`snakefmt --config {{path/to/config.toml}} {{path/to/snakefile}}`

- Formata um arquivo usando um comprimento máximo de linha específico:

`snakefmt --line-length 100 {{path/to/snakefile}}`

- Exibe às mudanças que seriam realizadas sem realiza-las:

`snakefmt --diff {{path/to/snakefile}}`
