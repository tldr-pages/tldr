# bc

> An arbitrary precision calculator language.
> See also: `dc`.
> More information: <https://keith.github.io/xcode-man-pages/bc.1.html>.

- Start an interactive session:

`bc`

- Start an interactive session with the standard math library enabled:

`bc --mathlib`

- Calculate an expression:

`bc --expression='{{5 / 3}}'`

- Execute a script:

`bc {{path/to/script.bc}}`

- Calculate an expression with the specified scale:

`bc --expression='scale = {{10}}; {{5 / 3}}'`

- Calculate a sine/cosine/arctangent/natural logarithm/exponential function using `mathlib`:

`bc --mathlib --expression='{{s|c|a|l|e}}({{1}})'`
