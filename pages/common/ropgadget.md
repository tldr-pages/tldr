# ROPgadget

> Find ROP gadgets in binary files.
> More information: <https://github.com/JonathanSalwan/ROPgadget>.

- List gadgets in the binary file:

`ROPgadget --binary {{path/to/binary}}`

- List gadgets in the binary file, filtered by regular expression:

`ROPgadget --binary {{path/to/binary}} --re {{regex}}`

- List gadgets in the binary file, excluding specified type:

`ROPgadget --binary {{path/to/binary}} --{{norop|nojob|nosys}}`

- List gadgets in the binary file, not including bad bytes:

`ROPgadget --binary {{path/to/binary}} --badbytes {{byte_string}}`

- List gadgets in the binary file, with up to a given number of bytes:

`ROPgadget --binary {{path/to/binary}} --depth {{nbyte}}`
