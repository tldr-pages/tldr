# snakefmt

> Formata arquivos Snakemake.
> Mais informações: <https://github.com/snakemake/snakefmt>.

- Formata um Snakefile:

`snakefmt {{path/to/snakefile}}`

- Formata todos os Snakefiles em uma pasta:

`snakefmt {{path/to/directory}}`

- Especifica um arquivo de configuração customizado:

`snakefmt --config {{path/to/config.toml}} {{path/to/snakefile}}`

- Especifica um comprimento máximo de linha customizado:

`snakefmt --line-length 100 {{path/to/snakefile}}`

- Exibe possíveis correções para cada arquivo sem alterá-los:

`snakefmt --diff {{path/to/snakefile}}`
