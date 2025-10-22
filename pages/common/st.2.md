# st

> Print basic descriptive statistics from input numbers.
> More information: <https://github.com/nferraz/st>.

- Print count, min, max, sum, mean, and standard deviation for numbers in a file:

`st {{path/to/file}}`

- Print statistics from `stdin`:

`cat {{path/to/file}} | st`

- Print only the sum of the numbers:

`st {{[-s|--sum]}} {{path/to/file}}`

- Print only the mean of the numbers:

`st {{[-m|--mean]}} {{path/to/file}}`

- Print only the standard deviation:

`st {{[-s|--sd]}} {{path/to/file}}`

- Transpose output (keys in one column, values in another):

`st {{[-t|--transpose]}} {{path/to/file}}`
