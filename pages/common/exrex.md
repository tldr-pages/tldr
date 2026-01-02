# exrex

> Generate all/random matching strings for a `regex`.
> It can also simplify `regex`es.
> More information: <https://github.com/asciimoo/exrex#usage>.

- Generate all possible strings that match a `regex`:

`exrex '{{regex}}'`

- Generate a random string that matches a `regex`:

`exrex {{[-r|--random]}} '{{regex}}'`

- Generate at most 100 strings that match a `regex`:

`exrex {{[-m|--max-number]}} {{100}} '{{regex}}'`

- Generate all possible strings that match a `regex`, joined by a custom delimiter string:

`exrex {{[-d|--delimiter]}} "{{, }}" '{{regex}}'`

- Print count of all possible strings that match a `regex`:

`exrex {{[-c|--count]}} '{{regex}}'`

- Simplify a `regex`:

`exrex {{[-s|--simplify]}} '{{ab|ac}}'`

- Print eyes:

`exrex '{{[oO0](_)[oO0]}}'`

- Print a boat:

`exrex '{{( {20}(\| *\\|-{22}|\|)|\.={50}| ( ){0,5}\\\.| {12}~{39})}}'`
