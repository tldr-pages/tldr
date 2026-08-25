# yamllint

> A linter for YAML files.
> More information: <https://yamllint.readthedocs.io>.

- Lint a file:

`yamllint {{path/to/file.yaml}}`

- Lint all YAML files in a directory recursively:

`yamllint {{path/to/directory}}`

- Lint a file with a specific config file:

`yamllint {{[-c|--config-file]}} {{path/to/config.yaml}} {{path/to/file.yaml}}`

- Lint a file using a preset config (`default` or `relaxed`):

`yamllint {{[-d|--config-data]}} "{{extends: relaxed}}" {{path/to/file.yaml}}`

- Output in a parsable format (for CI integration):

`yamllint {{[-f|--format]}} parsable {{path/to/file.yaml}}`

- Lint a file with strict mode (return 2 for warnings):

`yamllint {{[-s|--strict]}} {{path/to/file.yaml}}`

- Read from `stdin`:

`cat {{path/to/file.yaml}} | yamllint -`

- Display help:

`yamllint {{[-h|--help]}}`
