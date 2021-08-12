# rabin2

> Obțineți informații despre fișierele binare (ELF, PE, Java CLASS, Mach-O) - simboluri, secțiuni, biblioteci legate etc.
> Vine la pachet cu `radare2`.

- Afișați informații generale despre un binar (arhitectură, tip, endianness):

`rabin2 -I {{path/to/binary}}`

- Afișează bibliotecile legate:

`rabin2 -l {{path/to/binary}}`

- Afișează simbolurile importate din biblioteci:

`rabin2 -i {{path/to/binary}}`

- Afișează șiruri de caractere conținute în binar:

`rabin2 -z {{path/to/binary}}`

- Afișează ieșirea în JSON:

`rabin2 -j -I {{path/to/binary}}`
