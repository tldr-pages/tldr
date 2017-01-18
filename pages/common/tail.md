# [tail](http://man7.org/linux/man-pages/man1/tail.1.html)
> Display the last part of a file.

- Show last 'num' lines in file:

`tail -n {{num}} {{file}}`

- Show all file since line 'num':

`tail -n +{{num}} {{file}}`

- Show last 'num' bytes in file:

`tail -c {{num}} {{file}}`

- Keep reading file until ctrl-c:

`tail -f {{file}}`
