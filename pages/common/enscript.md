# enscript

> A tool to convert text files to PostScript, HTML, RTF, ANSI, and overstrikes.
> More information: <https://www.gnu.org/software/enscript>.

- Generate PostScript from a file and output to another:

`enscript {{path/to/input_file}} --output={{path/to/output_file}}`

- Generate a certain output language (eg. "html") from a file and output to another:

`enscript {{path/to/input_file}} --language={{language}} --output={{path/to/output_file}}`

- Generate PostScript from a file and output to another with 1 to 9 column per page in landscape:

`enscript {{path/to/input_file}} --columns={{num}} --landscape --output={{path/to/output_file}}`

- Display available syntax highlighting:

`enscript --help-highlight`

- Generate PostScript from a file and output to another with syntax highlighting and color for a specified language:

`enscript {{path/to/input_file}} --color=1 --highlight={{language}} --output={{path/to/output_file}}`
