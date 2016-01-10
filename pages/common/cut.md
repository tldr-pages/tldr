# cut

> Cut out fields from STDIN or files.

- Cut out the first sixteen characters of each line of STDIN:

`cut -c {{1-16}}`

- Cut out the first sixteen characters of each line of the given files:

`cut -c {{1-16}} {{file}}`

- Cut out everything from the 3rd character to the end of each line:

`cut -c{{3-}}`

- Cut out the fifth field, split on the colon character of each line:

`cut -d'{{:}}' -f{{5}}`

- Cut out the fields five and 10, split on the colon character of each line:

`cut -d'{{:}}' -f{{5,10}}`

- Cut out the fields five through 10, split on the colon character of each line:

`cut -d'{{:}}' -f{{5-10}}`
