# grex

> Generate `regex`s.
> More information: <https://github.com/pemistahl/grex>.

- Generate a simple `regex`:

`grex {{string1 string2 ...}}`

- Generate a case-insensitive `regex`:

`grex {{[-i|--ignore-case]}} {{string1 string2 ...}}`

- Replace digits with `\d`:

`grex {{[-d|--digits]}} {{string1 string2 ...}}`

- Replace Unicode word character with `\w`:

`grex {{[-w|--words]}} {{string1 string2 ...}}`

- Replace spaces with `\s`:

`grex {{[-s|--spaces]}} {{string1 string2 ...}}`

- Add {min, max} quantifier representation for repeating sub-strings:

`grex {{[-r|--repetitions]}} {{string1 string2 ...}}`

- Generate `regex` of test cases (separated by newline) from a file:

`grex {{[-f|--file]}} {{path/to/file}}`

- Do not generate anchors and non-capture groups:

`grex --no-anchors {{[-g|--capture-groups]}} {{string1 string2 ...}}`
