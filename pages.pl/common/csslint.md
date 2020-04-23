# csslint

> Linter dla kodu CSS.
> Więcej informacji: <https://github.com/CSSLint/csslint/wiki/Command-line-interface>.

- Lintowanie pojedynczego pliku CSS:

`csslint {{plik.css}}`

- Lintowanie wiele plików CSS:

`csslint {{plik1.css}} {{plik2.css}} {{plik3.css}}`

- Wymień wszystkie możliwe reguły stylu:

`csslint --list-rules`

- Określ pewne reguły jako błędy (które powodują niezerowy kod wyjścia):

`csslint --errors={{bledy,universal-selector,imports}} {{plik.css}}`

- Określ pewne reguły jako ostrzeżenia:

`csslint --warnings={{box-sizing,selector-max,floats}} {{plik.css}}`

- Określ pewne reguły, które będą całkowicie ignorowane:

`csslint --ignore={{ids,rules-count,shorthand}} {{plik.css}}`
