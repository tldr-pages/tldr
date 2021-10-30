# nm

> List symbol names in object files.

- List global (extern) functions in a file (prefixed with T):

`nm -g {{file.o}}`

- List only undefined symbols in a file:

`nm -u {{file.o}}`

- List all symbols, even debugging symbols:

`nm -a {{file.o}}`

- Demangle C++ symbols (make them readable):

`nm --demangle {{file.o}}`
