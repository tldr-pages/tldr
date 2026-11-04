# snakefmt

> Format Snakemake files.
> More information: <https://github.com/snakemake/snakefmt#usage>.

- Format a specific Snakefile:

`snakefmt {{path/to/snakefile}}`

- Format all Snakefiles recursively in a specific directory:

`snakefmt {{path/to/directory}}`

- Format a file using a specific configuration file:

`snakefmt --config {{path/to/config.toml}} {{path/to/snakefile}}`

- Format a file using a specific maximum line length:

`snakefmt --line-length {{100}} {{path/to/snakefile}}`

- Simulate formatting and display the changes that would be made:

`snakefmt --diff {{path/to/snakefile}}`
