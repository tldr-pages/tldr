# Less than

> Redirect data to `stdin`.
> More information: <https://gnu.org/software/bash/manual/bash.html#Redirecting-Input>.

- Redirect a file to `stdin` (achieves the same effect as `cat file.txt |`):

`{{command}} < {{path/to/file.txt}}`

- Create a here string and pass that in a file descriptor to `command`:

`{{command}} <<< {{string}}`
