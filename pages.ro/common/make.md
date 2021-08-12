# make

> Alergător de activități pentru țintele descrise în Makefile.
> Folosit în principal pentru a controla compilarea unui executabil din codul sursă.
> Mai multe informaţii: <https://www.gnu.org/software/make/manual/make.html>

- Apelați prima țintă specificată în Makefile (numită de obicei „toate”):

`make`

- Apelați o țintă specifică:

`make {{target}}`

- Apelați o țintă specifică, executând 4 locuri de muncă la un moment dat în paralel:

`make -j{{4}} {{target}}`

- Utilizați un anumit Makefile:

`make --file {{file}}`

- Executa face dintr-un alt director:

`make --directory {{directory}}`

- Forța de realizare a unei ținte, chiar dacă fișierele sursă sunt neschimbate:

`make --always-make {{target}}`

- Suprascrie variabilele definite în Makefile de mediu:

`make --environment-overrides {{target}}`
