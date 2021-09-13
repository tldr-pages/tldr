# po4a-translate

> Convert a PO file back to documentation format.
> The provided PO file should be the translation of the POT file which was produced by `po4a-gettextize`.
> More information: <https://po4a.org/man/man1/po4a-translate.1.php>.

- Convert a translated PO file back to a document:

`po4a-translate --format {{text}} --master {{path/to/master.doc}} --po {{path/to/result.po}} --localized {{path/to/translated.txt}}`

- Get a list of available formats:

`po4a-translate --help-format`
