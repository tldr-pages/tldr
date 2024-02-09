# csslint

> A linter for CSS code.
> More information: <https://github.com/CSSLint/csslint/wiki/Command-line-interface>.

- Lint a single CSS file:

`csslint {{file.css}}`

- Lint multiple CSS files:

`csslint {{file1.css file2.css ...}}`

- List all possible style rules:

`csslint --list-rules`

- Treat certain rules as errors (which results in a non-zero exit code):

`csslint --errors={{errors,universal-selector,imports}} {{file.css}}`

- Treat certain rules as warnings:

`csslint --warnings={{box-sizing,selector-max,floats}} {{file.css}}`

- Ignore specific rules:

`csslint --ignore={{ids,rules-count,shorthand}} {{file.css}}`
