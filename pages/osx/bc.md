# bc

> An arbitrary precision calculator language.
> Get help or version: bc --help|--version.
> More information: <https://manned.org/man/bc.1>.

- Start an interactive session:

`bc`

- Start an interactive session with the standard math library enabled:

`bc --mathlib`

- Calculate an expression:

`bc --expression='{{5 / 3}}'`

- Execute a script:

`bc {{path/to/file}}`

- Calculate an expression with the specified scale:

`bc --expression='scale = {{10}}; {{5 / 3}}'`

- Calculate a sine/cosine/arctangent/natural logarithm/exponential function using `mathlib`:

`bc --mathlib --expression='{{s|c|a|l|e}}({{1}})'`
