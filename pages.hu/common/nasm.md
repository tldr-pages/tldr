# nasm

> A Netwide Assembler, egy hordozható 80x86-os assembler. További információ: <https://nasm.us>.

- A `source.asm` összerakása a `source` bináris fájlba (alapértelmezett) nyers bináris formátumban:

`nasm {{source.asm}}`

- A `source.asm` összerakása a `output_file` bináris fájlba, a megadott formátumban:

`nasm -f {{format}} {{source.asm}} -o {{output_file}}`

- Az érvényes kimeneti formátumok listája (az alapvető nasm-segédlettel együtt):

`nasm -hf`

- Összeállítás és összeállítási listafájl létrehozása:

`nasm -l {{list_file}} {{source.asm}}`

- Az összeszerelés előtt hozzáad egy könyvtárat (a könyvtárat záróvesszővel kell írni) az include fájl keresési útvonalához:

`nasm -i {{path/to/include_dir/}} {{source.asm}}`
