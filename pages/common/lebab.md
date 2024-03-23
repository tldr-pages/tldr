# lebab

> A JavaScript modernizer for transpiling code to ES6/ES7.
> Transformations must be provided for all examples.
> More information: <https://github.com/lebab/lebab>.

- Transpile using one or more comma-separated transformations:

`lebab --transform {{transformation1,transformation2,...}}`

- Transpile a file to `stdout`:

`lebab {{path/to/input_file}}`

- Transpile a file to the specified output file:

`lebab {{path/to/input_file}} --out-file {{path/to/output_file}}`

- Replace all `.js` files in-place in the specified directory, glob or file:

`lebab --replace {{directory|glob|file}}`

- Display help:

`lebab --help`
