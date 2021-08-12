# filefrag

> Raportați cât de grav ar putea fi un anumit fișier.
> Mai multe informaţii: <https://manned.org/filefrag>

- Afișează un raport pentru un anumit fișier:

`filefrag {{path/to/file}}`

- Afișează un raport pentru lista de fișiere separate de spațiu:

`filefrag {{path/to/file1}} {{path/to/file2}}`

- Afișarea unui raport utilizând un bloc de 1024 octeți:

`filefrag -b {{path/to/file}}`

- Sincronizați fișierul înainte de a solicita cartografierea:

`filefrag -s {{path/to/files}}`

- Afișarea cartografierii atributelor extinse:

`filefrag -x {{path/to/files}}`

- Afișează un raport cu informații detaliate:

`filefrag -v {{path/to/files}}`
