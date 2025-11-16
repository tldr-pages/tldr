# grex

> Generate `regex`s.
> More information: <https://github.com/pemistahl/grex>.

- Generate a simple `regex`:

`grex {{space_separated_strings}}`

- Generate a case-insensitive `regex`:

`grex {{[-i|--ignore-case]}} {{space_separated_strings}}`

- Replace digits with '\d':

`grex {{[-d|--digits]}} {{space_separated_strings}}`

- Replace Unicode word character with '\w':

`grex {{[-w|--words]}} {{space_separated_strings}}`

- Replace spaces with '\s':

`grex {{[-s|--spaces]}} {{space_separated_strings}}`

- Add {min, max} quantifier representation for repeating sub-strings:

`grex {{[-r|--repetitions]}} {{space_separated_strings}}`

- Generate `regex` of test cases (separated by newline) from a file:

`grex {{[-f|--file]}} {{path/to/file}}`
