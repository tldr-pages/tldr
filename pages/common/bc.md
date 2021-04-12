# bc

> An arbitrary precision calculator language.
> More information: <https://manned.org/bc>.

- Start `bc` in interactive mode using the standard math library:

`bc -l`

- Calculate the result of an expression:

`bc <<< "(1 + 2) * 2 ^ 2"`

- Calculate the result of an expression and force the number of decimal places to 10:

`bc <<< "scale=10; 5 / 3"`

- Calculate the result of an expression with sine and cosine using `mathlib`:

`bc -l <<< "s(1) + c(1)"`
