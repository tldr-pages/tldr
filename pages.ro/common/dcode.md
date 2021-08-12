# dcode

> Detectează și decodează recursiv șiruri, suportând hash-uri hexagonal, zecimal, binar, base64, URL, dincodificări Char, cifruri Cezar și MD5, SHA1 și SHA2.
> Avertisment: utilizează servicii web terță parte pentru căutări hash MD5, SHA1 și SHA2. Pentru datele sensibile, utilizați `-s` pentru a evita aceste servicii.
> Mai multe informaţii: <https://github.com/s0md3v/Decodify>

- Detectarea și decodarea recursivă a unui șir de caractere:

`dcode "{{NjM3YTQyNzQ1YTQ0NGUzMg==}}"`

- Rotiți un șir cu decalajul specificat:

`dcode -rot {{11}} "{{spwwz hzcwo}}"`

- Rotiți un șir de toate cele 26 posibile compensări:

`dcode -rot {{all}} "{{bpgkta xh qtiitg iwpc sr}}"`

- Inversează un șir:

`dcode -rev "{{hello world}}"`
