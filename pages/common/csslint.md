# csslint

> A linter for CSS code.
> More information: <https://github.com/CSSLint/csslint/wiki/Command-line-interface>.

- Lint a single CSS file:

`csslint {{path/to/file.css}}`

- Lint multiple CSS files:

`csslint {{path/to/file1.css path/to/file2.css ...}}`

- List all possible style rules:

`csslint --list-rules`

- Specify certain rules as errors (which result in a non-zero exit code):

`csslint --errors={{errors,universal-selector,imports}} {{path/to/file.css}}`

- Specify certain rules as warnings:

`csslint --warnings={{box-sizing,selector-max,floats}} {{path/to/file.css}}`

- Specify certain rules to ignore:

`csslint --ignore={{ids,rules-count,shorthand}} {{path/to/file.css}}`
