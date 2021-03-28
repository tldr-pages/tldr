# expect

> Script executor that interacts with other programs that require user input.
> More information: <https://man7.org/linux/man-pages/man1/expect.1.html>.

- Execute an expect script from a file:

`expect {{path/to/file}}`

- Execute a specified expect script:

`expect -c "{{commands}}"`

- Enter an interactive REPL (use `exit` or Ctrl + D to exit):

`expect -i`
