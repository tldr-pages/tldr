# dolos

> Plagiarism detection for programming exercises.
> More information: <https://dolos.ugent.be>.

- Run a basic analysis:

`dolos run {{path/to/files/*}}`

- Run an analysis with a web server view:

`dolos run {{[-f|--output-format]}} web {{path/to/files/*}}`

- Specify the programming language:

`dolos run {{[-l|--language]}} {{language_name}} {{path/to/files/*}}`

- Ignore boilerplate/template code:

`dolos run {{[-i|--ignore]}} {{path/to/template_file}} {{path/to/files/*}}`

- Output a CSV report:

`dolos run {{[-f|--output-format]}} csv {{path/to/files/*}}`

- Serve an existing analysis report:

`dolos serve {{path/to/report_directory}}`

- Display help:

`dolos {{[-h|--help]}}`

- Display version:

`dolos {{[-v|--version]}}`
