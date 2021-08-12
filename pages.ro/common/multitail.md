# multitail

> Extensia cozii.
> Mai multe informaţii: <https://manned.org/multitail>

- Coadă toate fișierele care se potrivesc unui model într-un singur flux:

`multitail -Q 1 '{{pattern}}'`

- Coada toate fișierele într-un director într-un singur flux:

`multitail -Q 1 '{{directory}}/*'`

- Adaugă automat fișiere noi într-o fereastră:

`multitail -Q {{pattern}}`

- Afișați 5 fișiere de jurnal în timp ce fuzionați 2 și puneți-le în 2 coloane cu o singură în coloana din stânga:

`multitail -s 2 -sn 1,3 {{mergefile}} -I {{file1}} {{file2}} {{file3}} {{file4}}`
