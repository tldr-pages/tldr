# bc

> An arbitrary precision calculator language.
> See also: `dc`, `qalc`.
> More information: <https://manned.org/bc>.

- Start an interactive session:

`bc`

- Start an [i]nteractive session with the standard math [l]ibrary enabled:

`bc --interactive --mathlib`

- Calculate an expression:

`echo '{{5 / 3}}' | bc`

- Execute a script:

`bc {{path/to/script.bc}}`

- Calculate an expression with the specified scale:

`echo 'scale = {{10}}; {{5 / 3}}' | bc`

- Calculate a sine/cosine/arctangent/natural logarithm/exponential function using `mathlib`:

`echo '{{s|c|a|l|e}}({{1}})' | bc --mathlib`

- Execute an inline factorial script:

`echo "define factorial(n) { if (n <= 1) return 1; return n*factorial(n-1); }; factorial({{10}})" | bc`
