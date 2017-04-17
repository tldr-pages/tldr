# tail

> Display the last part of a file.

- Show last 'num' lines in file:

`tail -n {{num}} {{file}}`

- Show all file since line 'num':

`tail -n +{{num}} {{file}}`

- Show last 'num' bytes in file:

`tail -c {{num}} {{file}}`

- Keep reading file until ctrl-c:

`tail -f {{file}}`

- show last 100 lines of file and keep reading file until ctrl-c
 
`tail -100f {{file}}`
