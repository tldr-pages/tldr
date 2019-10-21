# expect

> Script executor that interacts with other programs that require user input.
> More information: <https://linux.die.net/man/1/expect>.

- Execute an expect script from a file:

`expect {{path/to/file}}`

- Execute a specified expect script:

`expect -c "{{commands}}"`

- Enter an interactive REPL (use `exit` or Ctrl + D to exit):

`expect -i`
