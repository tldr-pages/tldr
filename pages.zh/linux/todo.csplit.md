# csplit

> Split a file into pieces.
> This generates files named "xx00", "xx01", and so on.

- Split a file at lines 5 and 23:

`csplit {{file}} {{5}} {{23}}`

- Split a file every 5 lines (this will fail if the total number of lines is not divisible by 5):

`csplit {{file}} {{5}} {*}`

- Split a file every 5 lines, ignoring exact-division error:

`csplit -k {{file}} {{5}} {*}`

- Split a file at line 5 and use a custom prefix for the output files:

`csplit {{file}} {{5}} -f {{prefix}}`

- Split a file at a line matching a regular expression:

`csplit {{file}} /{{regex}}/`
