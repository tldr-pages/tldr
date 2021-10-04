# cat

> Print the contents of any file to STDOUT.
> More information: <https://www.gnu.org/software/coreutils/cat>

- Print the contents of a file in your current directory:

`cat {{file.ext}}`

- Print the contents of a file in another directory:

`cat {{path/to/file.ext}}`

- Print the contents of a file and number the lines:

`cat -n {{file.ext}}`

- Print the contents of a file and number only non-empty lines:

`cat -b {{file.ext}}
