# po4a-gettextize

> Convert a file to a PO file.
> More information: <https://po4a.org/man/man1/po4a-gettextize.1.php>.

- Convert a text file to PO file:

`po4a-gettextize --format {{text}} --master {{path/to/master.txt}} --po {{path/to/result.po}}`

- Get a list of available formats:

`po4a-gettextize --help-format`

- Convert a text file along with a translated document to a PO file (`-l` option can be provided multiple times):

`po4a-gettextize --format {{text}} --master {{path/to/master.txt}} --localized {{path/to/translated.txt}} --po {{path/to/result.po}}`
