# envsubst

> Substitutes environment variables with their value in shell format strings.
> Variables to be replaced should be in either `${var}` or `$var` format.

- Replace environment variables in `stdin` and output to `stdout`:

`echo '{{$HOME}}' | envsubst`

- Replace environment variables in an input file and output to `stdout`:

`envsubst < {{path/to/input_file}}`

- Replace environment variables in an input file and output to a file:

`envsubst < {{path/to/input_file}} > {{path/to/output_file}}`

- Replace environment variables in an input file from a space-separated list:

`envsubst '{{$USER $SHELL $HOME}}' < {{path/to/input_file}}`
