# bc

> An arbitrary precision calculator language.
> Get help or version: bc --help|--version.
> More information: <https://manned.org/man/bc.1>.

- Start `bc` in interactive mode using the standard math library:

`bc --mathlib`

- Calculate the result of an expression:

`echo '(1 + 2) * 2 ^ 2' | bc`

- Calculate the result of an expression and force the number of decimal places to 10:

`echo 'scale=10; 5 / 3' | bc`

- Calculate the result of an expression with sine and cosine using `mathlib`:

`echo 's(1) + c(1)' | bc --mathlib`
