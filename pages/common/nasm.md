# nasm

> The Netwide Assembler, a portable 80x86 assembler.

- Assemble binary file `source` of raw binary format from `source.asm`:

`nasm {{source.asm}}`

- Assemble binary file `output_file` of the specified format:

`nasm -f {{format}} {{source.asm}} -o {{output_file}}`

- View valid output formats (along with basic nasm help):

`nasm -hf`

- Assemble and generate an assembly listing file:

`nasm -l {{list_file}} {{source.asm}}`

- Add a directory (written with trailing slash) to the include file search path before assembling:

`nasm -i {{/path/to/include_dir/}} {{source.asm}}`
