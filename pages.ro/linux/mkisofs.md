# mkisofs

> Creați fișiere ISO din directoare.
> De asemenea, aliasat ca „genisoimage`”.

- Creați un ISO dintr-un director:

`mkisofs -o {{filename.iso}} {{path/to/source_directory}}`

- Setați eticheta discului atunci când creați un ISO:

`mkisofs -o {{filename.iso}} -V "{{label_name}}" {{path/to/source_directory}}`
