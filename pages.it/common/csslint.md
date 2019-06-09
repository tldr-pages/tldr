# csslint

> Un linter per codice CSS.
> Maggiori informazioni: <https://github.com/CSSLint/csslint/wiki/Command-line-interface>.

- Esegui il linting di un singolo file CSS:

`csslint {{file.css}}`

- Esegui il linting di file CSS multipli:

`csslint {{file1.css}} {{file2.css}} {{file3.css}}`

- Elenca tutte le possibili regole di stile:

`csslint --list-rules`

- Specifica certe regole come errori (che risulteranno in un codice d'uscita diverso da zero):

`csslint --errors={{errors,universal-selector,imports}} {{file.css}}`

- Specifica certe regole come warning:

`csslint --warnings={{box-sizing,selector-max,floats}} {{file.css}}`

- Specifica certe regole da essere completamente ignorate:

`csslint --ignore={{ids,rules-count,shorthand}} {{file.css}}`
