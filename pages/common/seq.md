# seq

> Output a sequence of numbers to `stdout`.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/seq-invocation.html>.

- Print a sequence from 1 to 10:

`seq 10`

- Print a sequence from 10 to 20:

`seq 10 20`

- Print every 3rd number from 5 to 20:

`seq 5 3 20`

- Separate the output with a space instead of a newline:

`seq {{[-s|--separator]}} " " {{5 3 20}}`

- Format output width to a minimum of 4 digits padding with zeros as necessary:

`seq {{[-f|--format]}} "%04g" {{5 3 20}}`

- Print all numbers with the same width:

`seq {{[-w|--equal-width]}} {{5 3 20}}`
