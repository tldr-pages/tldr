# wc

> Numără linii, cuvinte sau octeți.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/wc>

- Numără linii în fișier:

`wc -l {{file}}`

- Numără cuvintele în fișier:

`wc -w {{file}}`

- Numărați caracterele (octeții) în fișier:

`wc -c {{file}}`

- Numărați caracterele din fișier (luând în considerare seturi de caractere multi-octet):

`wc -m {{file}}`

- Utilizați intrarea standard pentru a număra linii, cuvinte și caractere (octeți) în această ordine:

`{{find .}} | wc`
