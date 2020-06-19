# sponge

> Soak up standard input and write to a file.
> Sponge soaks up all its input before writing the output file.

- Appended all file content to its origin file:

`cat {{path/to/file}} | sponge -a {{/path/to/file}}`

- Remove all line start with # in file:

`grep -v '^#' {{path/to/file}} | sponge {{/path/to/file}}`
