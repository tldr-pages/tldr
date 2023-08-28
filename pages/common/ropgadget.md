# ROPgadget

> Find ROP gadgets in binary files.
> More information: <https://github.com/JonathanSalwan/ROPgadget>.

- List gadgets in the binary:

`ROPgadget --binary {{path/to/binary}}`

- List gadgets in the binary filtered by regular expression:

`ROPgadget --binary {{path/to/binary}} --re {{regex}}`

- List gadgets in the binary excluding specified type:

`ROPgadget --binary {{path/to/binary}} --{{norop|nojob|nosys}}`

- List gadgets in the binary not including bad bytes:

`ROPgadget --binary {{path/to/binary}} --badbytes {{byte_string}}`

- List gadgets in the binary with up to given bytes:

`ROPgadget --binary {{path/to/binary}} --depth {{nbyte}}`
