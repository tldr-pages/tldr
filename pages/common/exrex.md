# exrex

> Generate all/random matching strings for a `regex`.
> It can also simplify `regex`es.
> More information: <https://github.com/asciimoo/exrex>.

- Generate all possible strings that match a `regex`:

`exrex '{{regex}}'`

- Generate a random string that matches a `regex`:

`exrex --random '{{regex}}'`

- Generate at most 100 strings that match a `regex`:

`exrex --max-number {{100}} '{{regex}}'`

- Generate all possible strings that match a `regex`, joined by a custom delimiter string:

`exrex --delimiter "{{, }}" '{{regex}}'`

- Print count of all possible strings that match a `regex`:

`exrex --count '{{regex}}'`

- Simplify a `regex`:

`exrex --simplify '{{ab|ac}}'`

- Print eyes:

`exrex '{{[oO0](_)[oO0]}}'`

- Print a boat:

`exrex '{{( {20}(\| *\\|-{22}|\|)|\.={50}| ( ){0,5}\\\.| {12}~{39})}}'`
