# hexdump

> O imagine octală ASCII, zecimală, hexazecimal.

- Imprimați reprezentarea hexazecimal a unui fișier:

`hexdump {{file}}`

- Afișează decalajul de intrare în hexazecimal și reprezentarea ASCII în două coloane:

`hexdump -C {{file}}`

- Afișați reprezentarea hexazecimală a unui fișier, dar interpretați numai n octeți ai intrării:

`hexdump -C -n{{number_of_bytes}} {{file}}`
