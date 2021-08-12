# lrztar

> Un ambalaj pentru `lrzip `pentru a simplifica compresia directoarelor.
> A se vedea, de asemenea: `tar`, `lrzuntar`, `lrunzip `.

- Arhivați un director cu `tar`, apoi comprimați:

`lrztar {{path/to/directory}}`

- La fel ca mai sus, cu ZPAQ - compresie extremă, dar foarte lent:

`lrztar -z {{path/to/directory}}`

- Specificați fișierul de ieșire:

`lrztar -o {{path/to/file}} {{path/to/directory}}`

- Suprascrie numărul de fire de procesor pentru a utiliza:

`lrztar -p {{8}} {{path/to/directory}}`

- Suprascrierea forțată a fișierelor existente:

`lrztar -f {{path/to/directory}}`
