# pass

> Instrument pentru stocarea și citirea parolelor sau a altor date sensibile.
> Toate datele sunt criptate GPG și gestionate cu un depozit Git.
> Mai multe informaţii: <https://www.passwordstore.org>

- Inițializați (sau re-criptați) spațiul de stocare utilizând unul sau mai multe ID-uri GPG:

`pass init {{gpg_id_1}} {{gpg_id_2}}`

- Salvați o parolă nouă și informații suplimentare (apăsați Ctrl + D pe o linie nouă pentru a finaliza):

`pass insert --multiline {{path/to/data}}`

- Editează o intrare:

`pass edit {{path/to/data}}`

- Copiați o parolă (prima linie a fișierului de date) în clipboard:

`pass -c {{path/to/data}}`

- Listează întregul arbore al magazinului:

`pass`

- Generați o nouă parolă aleatoare cu o anumită lungime și copiați-o în clipboard:

`pass generate -c {{path/to/data}} {{num}}`

- Inițializați un nou depozit Git (orice modificări efectuate prin trecere vor fi comise automat):

`pass git init`
