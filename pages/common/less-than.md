# Less than

> Redirect data to `stdin`.
> More information: <https://gnu.org/software/bash/manual/bash.html#Redirecting-Input>.

- Redirect a file to `stdin` (achieves the same effect as `cat file.txt |`):

`{{command}} < {{path/to/file.txt}}`

- Create a here document and pass that into `stdin` (requires a multiline command):

`{{command}} << {{EOF}} <Enter> {{multiline_data}} <Enter> {{EOF}}`

- Create a here string and pass that into `stdin` (achieves the same effect as `echo string |`):

`{{command}} <<< {{string}}`
