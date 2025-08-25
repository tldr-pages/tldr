# <>

> Open a file descriptor for read and write.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#Opening-File-Descriptors-for-Reading-and-Writing>.

- Open a file in a file descriptor for read an write:

`exec {{3}}<>{{path/to/file}}`

- Open a file descriptor to a remote connection:

`exec {{3}}<>/dev/{{tcp}}/{{remote_host}}/{{port_number}}`

- Close a file descriptor:

`exec {{3}}<>-`
