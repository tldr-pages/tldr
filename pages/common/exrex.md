# exrex

> Generate all/random matching strings for a regular expression.
> It can also simplify regular expressions.
> More information: <https://github.com/asciimoo/exrex>.

- Generate all possible strings that match a regular expression:

`exrex '{{regular_expression}}'`

- Generate a random string that matches a regular expression:

`exrex {{[-r|--random]}} '{{regex}}'`

- Generate at most 100 strings that match a regular expression:

`exrex {{[-m|--max-number]}} {{100}} '{{regex}}'`

- Generate all possible strings that match a regular expression, joined by a custom delimiter string:

`exrex {{[-d|--delimiter]}} "{{, }}" '{{regex}}'`

- Print count of all possible strings that match a regular expression:

`exrex {{[-c|--count]}} '{{regex}}'`

- Simplify a regular expression:

`exrex {{[-s|--simplify]}} '{{ab|ac}}'`

- Print eyes:

`exrex '{{[oO0](_)[oO0]}}'`

- Print a boat:

`exrex '{{( {20}(\| *\\|-{22}|\|)|\.={50}| ( ){0,5}\\\.| {12}~{39})}}'`
