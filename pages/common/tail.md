# tail

> Display the last part of a file

- show last 'num' lines in file

`tail -n {{num}} {{file}}`

- show all file since line 'num'

`tail -n +{{num}} {{file}}`

- show last 'num' bytes in file

`tail -c {{num}} {{file}}`

- keep reading file until ctrl-c

`tail -f {{file}}`

- show last 100 lines of file and keep reading file until ctrl-c
 
`tail -100f {{file}}`
