# biber

> A backend bibliography processor for the `biblatex` package.
> See also: `latexmk`.
> More information: <https://texdoc.org/serve/biber.pdf/0#section.3>.

- Generate bibliography data using a BibLaTeX Control File:

`biber {{path/to/file.bcf}}`

- Generate bibliography data using a configuration file:

`biber {{path/to/file.bcf}} {{[-g|--configfile]}} {{path/to/config_file}}`

- Enable debugging:

`biber {{path/to/file.bcf}} {{[-D|--debug]}}`
