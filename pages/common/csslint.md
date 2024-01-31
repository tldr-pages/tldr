# csslint

> A linter for CSS code.
> More information: <https://github.com/CSSLint/csslint/wiki/Command-line-interface>.

- Lint a single CSS file:

`csslint {{file.css}}`

- Lint multiple CSS files:

`csslint {{file1.css file2.css ...}}`

- List all possible style rules:

`csslint --list-rules`

- Specify certain rules as errors (which result in a non-zero exit code):

`csslint --errors={{errors,universal-selector,imports}} {{file.css}}`

- Specify certain rules as warnings:

`csslint --warnings={{box-sizing,selector-max,floats}} {{file.css}}`

- Specify certain rules to ignore:

`csslint --ignore={{ids,rules-count,shorthand}} {{file.css}}`
