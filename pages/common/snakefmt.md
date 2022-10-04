# snakefmt

> Provides formatting for [Snakemake](https://snakemake.readthedocs.io/) files.
> More information: <https://github.com/snakemake/snakefmt#full-usage>.

- Formats a single Snakefile:

`snakefmt {{path/to/snakefile}}`

- Formats all Snakefiles within a directory:

`snakefmt {{path/to/directory}}`

- Specify a custom configuration file:

`snakefmt --config {{path/to/config.toml}} {{path/to/snakefile}}`

- Specify a custom maximum line length:

`snakefmt --line-length 100 {{path/to/snakefile}}`

- Output possible fixes for each file without making changes to them:

`snakefmt --diff {{path/to/snakefile}}`
