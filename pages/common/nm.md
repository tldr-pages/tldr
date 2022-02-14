# nm

> List symbol names in object files.
> More information: <https://manned.org/nm>.

- List global (extern) functions in a file (prefixed with T):

`nm -g {{path/to/file.o}}`

- List only undefined symbols in a file:

`nm -u {{path/to/file.o}}`

- List all symbols, even debugging symbols:

`nm -a {{path/to/file.o}}`

- Demangle C++ symbols (make them readable):

`nm --demangle {{path/to/file.o}}`
