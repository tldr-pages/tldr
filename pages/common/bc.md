# bc

> Calculator.

- Run calculator in interactive mode:

`bc -i`

- Calculate the result of an expression:

`bc <<< "(1 + 2) * 2 ^ 2"`

- Calculate with the given precision:

`bc <<< "scale=10; 5 / 3"`

- Calculate expression with sine and cosine using mathlib:

`bc -l <<< "s(1) + c(1)"`
