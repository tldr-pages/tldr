# csslint

> Un linter pentru codul CSS.
> Mai multe informaţii: <https://github.com/CSSLint/csslint/wiki/Command-line-interface>

- Lint un singur fișier CSS:

`csslint {{file.css}}`

- Lint mai multe fisiere CSS:

`csslint {{file1.css}} {{file2.css}} {{file3.css}}`

- Listează toate regulile de stil posibile:

`csslint --list-rules`

- Specificați anumite reguli ca erori (care au ca rezultat un cod de ieșire diferit de zero):

`csslint --errors={{errors,universal-selector,imports}} {{file.css}}`

- Specificați anumite reguli ca avertismente:

`csslint --warnings={{box-sizing,selector-max,floats}} {{file.css}}`

- Specificați anumite reguli pentru a ignora complet:

`csslint --ignore={{ids,rules-count,shorthand}} {{file.css}}`
