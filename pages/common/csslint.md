# csslint

> A linter for CSS code.

- Lint a single CSS file:

`csslint {{file.css}}`

- Lint multiple CSS files:

`csslint {{file1.css}} {{file2.css}} {{file3.css}}`

- List all possible style rules:

`csslint --list-rules`

- Specify certain rules as errors (which result in a non-zero exit code):

`csslint --errors={{errors,universal-selector,imports}} {{file.css}}`

- Specify certain rules as warnings:

`csslint --warnings={{box-sizing,selector-max,floats}} {{file.css}}`

- Specify certain rules to completely ignore:

`csslint --ignore={{ids,rules-count,shorthand}} {{file.css}}`
