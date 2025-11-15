# eva

> Simple calculator REPL, similar to `bc`, with syntax highlighting and persistent history.
> More information: <https://github.com/NerdyPepper/eva>.

- Run the calculator in interactive mode:

`eva`

- Calculate the result of an expression:

`eva "{{(1 + 2) * 2 ^ 2}}"`

- Calculate an expression forcing the number of decimal places to 5:

`eva --fix {{5}} "{{5 / 3}}"`

- Calculate an expression with sine and cosine:

`eva "{{sin(1) + cos(1)}}"`
