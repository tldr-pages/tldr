# nm

> List symbol names in object files.

- List global (extern) functions in a file (prefixed with T:

`nm -g {{file.o}}`

- Demangle C++ symbols (make them readable:

`nm --demangle {{file.o}}`

- List only undefined symbols in a fil:

`nm -u {{file.o}}`

- List all symbols, even debugging symbol:

`nm -a {{file.o}}`
