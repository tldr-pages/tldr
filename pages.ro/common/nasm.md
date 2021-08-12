# nasm

> Monitorul Netwide, un asamblor portabil 80x86.
> Mai multe informaţii: <https://nasm.us>

- Asamblați `surce.asm` într-un fișier binar `surse`, în formatul binar brut (implicit):

`nasm {{source.asm}}`

- Asamblarea `source.asm` intr-un fisier binar `output_file`, in formatul specificat:

`nasm -f {{format}} {{source.asm}} -o {{output_file}}`

- Lista formatelor de ieșire valide (împreună cu ajutorul nasm de bază):

`nasm -hf`

- Asamblarea și generarea unui fișier de listă de asamblare

`nasm -l {{list_file}} {{source.asm}}`

- Adăugați un director (trebuie scris cu slash la final) la calea de căutare include fișiere înainte de asamblare:

`nasm -i {{path/to/include_dir/}} {{source.asm}}`
