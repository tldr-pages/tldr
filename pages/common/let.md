# let

> Evaluate arithmetic expressions in shell.
> Supports variables, operators, and conditional expressions.
> More information: <https://manned.org/let>.

- Evaluate a simple arithmetic expression:

`let "{{result = a + b}}"`

- Use post-increment and assignment in an expression:

`let "{{x++}}"`

- Use conditional operator in an expression:

`let "{{result = (x > 10) ? x : 0}}"`

- Display help:

`let --help`
