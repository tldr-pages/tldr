# base64

> Enkoduj lub dekoduj plik lub standardowe wejście do/z Base64, na standardowe wyjście.

- Enkoduj plik:

`base64 {{filename}}`

- Dekoduj plik:

`base64 -d {{filename}}`

- Enkoduj z `stdin`:

`{{somecommand}} | base64`

- Dekoduj z `stdin`:

`{{somecommand}} | base64 -d`
