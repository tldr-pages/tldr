# cut

> Cut out fields from STDIN

- Cut out the first sixteen characters of each line of STDIN

`cut -c 1-16`

- Cut out the fifth field, split on the colon character of each line in `file`

`cut -d':' -f5 file`

- Cut out the fields five and 10, split on the colon character of each line in `file`

`cut -d':' -f5,10 file`

- Cut out the fields five through 10, split on the colon character of each line in `file`

`cut -d':' -f5-10 file`

  Cut out everything from the 3rd character to the end of each line

`cut -c3- test.txt`
