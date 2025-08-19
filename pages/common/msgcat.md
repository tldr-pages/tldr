# msgcat

> Concatenate and merge multiple `.po` translation files.
> Useful in software localization pipelines to combine message catalogs with filtering options.
> More information: <https://www.gnu.org/software/gettext/manual/gettext.html#msgcat-Invocation>.

- Combine multiple `.po` files into one:

`msgcat {{file1.po file2.po ...}} {{[-o|--output-file]}} {{combined.po}}`

- Combine input files listed in a text file:

`msgcat {{[-f|--files-from]}} {{path/to/file_list.txt}} {{[-o|--output-file]}} {{combined.po}}`

- Set the output encoding (e.g. UTF-8):

`msgcat {{[-t|--to-code]}} {{UTF-8}} {{input.po}} {{[-o|--output-file]}} {{output.po}}`

- Output only unique messages (appearing in one file only):

`msgcat {{[-u|--unique]}} {{file1.po file2.po ...}} {{[-o|--output-file]}} {{unique.po}}`

- Use the first available translation for duplicate entries:

`msgcat --use-first {{file1.po file2.po ...}} {{[-o|--output-file]}} {{output.po}}`

- Display help:

`msgcat {{[-h|--help]}}`
