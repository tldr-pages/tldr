# envsubst

> Substitutes shell format strings with environment variables in text.
> Strings to be replaced should be in either `${var}` or `$var` format.

- Replace environment variables in stdin and output to `stdout`:

`echo '{{$HOME}}' | envsubst`

- Replace environment variables in an input file and output to `stdout`:

`envsubst < {{path/to/input}}`

- Replace environment variables in an input file and output to a file:

`envsubst < {{path/to/input}} > {{path/to/output}}`

- Replace environment variables in input from a space-separated list:

`envsubst {{variables}} < {{path/to/input}}`
