# csslint

> Linter dla kodu CSS.
> Więcej informacji: <https://github.com/CSSLint/csslint/wiki/Command-line-interface>.

- Lintowanie pojedynczego pliku CSS:

`csslint {{file.css}}`

- Lintowanie wiele plików CSS:

`csslint {{file1.css}} {{file2.css}} {{file3.css}}`

- Wymień wszystkie możliwe reguły stylu:

`csslint --list-rules`

- Określ pewne reguły jako błędy (które powodują niezerowy kod wyjścia):

`csslint --errors={{errors,universal-selector,imports}} {{file.css}}`

- Określ pewne reguły jako ostrzeżenia:

`csslint --warnings={{box-sizing,selector-max,floats}} {{file.css}}`

- Określ pewne reguły, które będą całkowicie ignorowane:

`csslint --ignore={{ids,rules-count,shorthand}} {{file.css}}`
