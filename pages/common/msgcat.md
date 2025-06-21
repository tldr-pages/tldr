# msgcat

> Concatenate and merge multiple `.po` translation files.
> Useful in software localization pipelines to combine message catalogs with filtering options.
> More information: <https://www.gnu.org/software/gettext/manual/html_node/msgcat-Invocation.html>.

- Combine multiple `.po` files into one:

`msgcat {{file1.po file2.po ...}} > {{combined.po}}`

- Combine input files listed in a text file:

`msgcat {{--files-from=file_list.txt}} > {{combined.po}}`

- Set the output encoding (e.g., UTF-8):

`msgcat --to-code {{UTF-8}} {{input.po}} > {{output.po}}`

- Output only unique messages (appearing in one file only):

`msgcat {{--unique}} {{file1.po}} {{file2.po}} > {{unique.po}}`

- Use the first available translation for duplicate entries:

`msgcat {{--use-first}} {{file1.po}} {{file2.po}} > {{output.po}}`

- Display help:

`msgcat {{--help}}`
