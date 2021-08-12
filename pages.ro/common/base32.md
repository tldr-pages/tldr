# base32

> Codificați sau decodificați fișierul sau intrarea standard la/de la Base32, la ieșirea standard.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/base32>

- Codifică un fișier:

`base32 {{filename}}`

- Descodifică un fişier:

`base32 --decode {{filename}}`

- Codifică din stdin:

`{{somecommand}} | base32`

- decodare de la stdin:

`{{somecommand}} | base32 --decode`
