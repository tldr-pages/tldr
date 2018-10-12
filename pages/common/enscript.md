# enscript

> A tool to convert text files to PostScript, HTML, RTF, ANSI, and overstrikes

- Generate PostScript from a file and output to another:

`enscript {{text_file}} --output={{output_file}}`

- Generate a certain output language (eg. _html_) from a file and output to another:

`enscript {{text_file}} --language={{language}} --output={{output_file}}`

- Generate PostScript from a file and output to another with 1 to 9 coloums per page in landscape:

`enscript {{text_file}} --columns={{num}} --landscape --output={{output_file}}`

- Display avaliable syntax highlighting:

`enscript --help-highlight`

- Genereate PostScript from a file and output to another with syntax highlighting and color for a specified language:

`enscript {{text_file}} --color=1 --highlight={{language}} --output={{output_file}}`
