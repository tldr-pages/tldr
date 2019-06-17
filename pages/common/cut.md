# cut

> Cut out fields from `stdin` or files.

- Cut out the first sixteen characters of each line of `stdin`:

`cut -c {{1-16}}`

- Cut out the first sixteen characters of each line of the given files:

`cut -c {{1-16}} {{file}}`

- Cut out everything from the 3rd character to the end of each line:

`cut -c {{3-}}`

- Cut out the fifth field of each line, using a colon as a field delimiter (default delimiter is tab):

`cut -d'{{:}}' -f{{5}}`

- Cut out the 2nd and 10th fields of each line, using a semicolon as a delimiter:

`cut -d'{{;}}' -f{{2,10}}`

- Cut out the fields 3 through to the end of each line, using a space as a delimiter:

`cut -d'{{ }}' -f{{3-}}`
