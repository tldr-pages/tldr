# base64

> Codificați sau decodificați fișierul sau intrarea standard la/de la Base64, la ieșirea standard.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/base64>

- Codificați conținutul unui fișier ca base64 și scrieți rezultatul la stdout:

`base64 {{filename}}`

- Descodificați conținutul base64 al unui fișier și scrieți rezultatul la stdout:

`base64 --decode {{filename}}`

- Codifică din stdin:

`{{somecommand}} | base64`

- decodare de la stdin:

`{{somecommand}} | base64 --decode`
