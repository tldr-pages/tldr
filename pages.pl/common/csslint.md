# csslint

> Lintuj kod CSS.
> Więcej informacji: <https://github.com/CSSLint/csslint/wiki/Command-line-interface>.

- Lintuj pojedyńczy plik CSS:

`csslint {{plik.css}}`

- Lintuj wiele plików CSS:

`csslint {{plik1.css plik2.css ...}}`

- Wymień wszystkie możliwe reguły stylu:

`csslint --list-rules`

- Określ pewne reguły jako błędy (które powodują niezerowy kod wyjścia):

`csslint --errors={{errors,universal-selector,imports}} {{plik.css}}`

- Określ pewne reguły jako ostrzeżenia:

`csslint --warnings={{box-sizing,selector-max,floats}} {{plik.css}}`

- Ignoruj określone reguły:

`csslint --ignore={{ids,rules-count,shorthand}} {{plik.css}}`
