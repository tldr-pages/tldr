# snakefmt

> Formata arquivos [Snakemake](https://snakemake.readthedocs.io/).
> Mais informações: <https://github.com/snakemake/snakefmt#full-usage>.

- Formatar um Snakefile:

`snakefmt {{path/to/snakefile}}`

- Formatar todos os Snakefiles em uma pasta:

`snakefmt {{path/to/directory}}`

- Especificar um arquivo de configuração customizado:

`snakefmt --config {{path/to/config.toml}} {{path/to/snakefile}}`

- Especificar um comprimento máximo de linha customizado:

`snakefmt --line-length 100 {{path/to/snakefile}}`

- Exibir possíveis correções para cada arquivo sem alterá-los:

`snakefmt --diff {{path/to/snakefile}}`
