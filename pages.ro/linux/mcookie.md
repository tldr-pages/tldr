# mcookie

> Generează numere hexazecimale aleatoare 128 de biți.

- Generează un număr aleator:

`mcookie`

- Generează un număr aleatoriu, folosind conținutul unui fișier ca sămânță pentru aleatoriu:

`mcookie --file {{path/to/file}}`

- Generează un număr aleatoriu, folosind un anumit număr de octeți dintr-un fișier ca sămânță pentru aleatoriu:

`mcookie --file {{path/to/file}} --max-size {{number_of_bytes}}`

- Imprimați detaliile aleatorii utilizate, cum ar fi originea și semințele pentru fiecare sursă:

`mcookie --verbose`
