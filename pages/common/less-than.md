# <

> Redirect data to `stdin`.
> More information: <https://gnu.org/software/bash/manual/bash.html#Redirecting-Input>.

- Redirect a file to `stdin` (achieves the same effect as `cat file.txt |`):

`{{command}} < {{path/to/file.txt}}`

- Create a here document and pass that into `stdin` (requires a multiline command):

`{{command}} << {{EOF}} <Enter> {{multiline_text}} <Enter> {{EOF}}`

- Create a here string and pass that into `stdin` (achieves the same effect as `echo string |`):

`{{command}} <<< {{string}}`

- Process data from a file and write the output to another file:

`{{command}} < {{path/to/file.txt}} > {{path/to/file2.txt}}`

- Write a here document into a file:

`cat << {{EOF}} > {{path/to/file.txt}} <Enter> {{multiline_data}} <Enter> {{EOF}}`

- Disregard leading tabs (good for scripts with indentation but does not work for spaces):

`cat <<- {{EOF}} > {{path/to/file.txt}} <Enter> {{multiline_data}} <Enter> {{EOF}}`

- Pass command output to a program as a file descriptor:

`diff <({{command1}}) <({{command2}})`

- Open a persistent file descriptor:

`exec {{3}}<{{path/to/file}}`
