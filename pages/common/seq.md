# seq

> Output a sequence of numbers to stdout.
> More information: <https://www.gnu.org/software/coreutils/seq>.

- Sequence from 1 to 10:

`seq 10`

- Every 3rd number from 5 to 20:

`seq 5 3 20`

- Separate the output with a space instead of a newline:

`seq -s " " 5 3 20`

- Format output width to a minimum of 4 digits padding with zeros as necessary:

`seq -f "%04g" 5 3 20`
