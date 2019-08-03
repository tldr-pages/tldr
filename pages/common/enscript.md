# enscript

> Convert text files to PostScript, HTML, RTF, ANSI, and overstrikes.
> More information: <https://www.gnu.org/software/enscript>.

- Generate a PostScript file from a text file:

`enscript {{path/to/input_file}} --output={{path/to/output_file}}`

- Generate a file in a different language than PostScript:

`enscript {{path/to/input_file}} --language={{html|rtf|...}} --output={{path/to/output_file}}`

- Generate a PostScript file with a landscape layout, splitting the page into columns (maximum 9):

`enscript {{path/to/input_file}} --columns={{num}} --landscape --output={{path/to/output_file}}`

- Display available syntax highlighting languages and file formats:

`enscript --help-highlight`

- Generate a PostScript file with syntax highlighting and color for a specified language:

`enscript {{path/to/input_file}} --color=1 --highlight={{language}} --output={{path/to/output_file}}`
