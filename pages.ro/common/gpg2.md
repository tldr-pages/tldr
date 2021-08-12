# gpg2

> GNU Privacy Guard 2.
> Vezi `gpg` pentru GNU Privacy Guard 1.
> Mai multe informaţii: <https://docs.releng.linuxfoundation.org/en/latest/gpg.html>

- Lista cheilor importate:

`gpg2 --list-keys`

- Criptați un fișier specificat pentru un destinatar specificat, scriind ieșirea într-un fișier nou cu `.gpg` adăugat:

`gpg2 --encrypt --recipient {{alice@example.com}} {{path/to/doc.txt}}`

- Criptați un fișier specificat cu doar o frază de acces, scriind ieșirea într-un fișier nou cu `.gpg` adăugat:

`gpg2 --symmetric {{path/to/doc.txt}}`

- Decripta un fișier specificat, scriind rezultatul la ieșirea standard:

`gpg2 --decrypt {{path/to/doc.txt.gpg}}`

- Importați o cheie publică:

`gpg2 --import {{path/to/public_key.gpg}}`

- Exportați cheia publică a unei adrese de e-mail specificate la ieșirea standard:

`gpg2 --export --armor {{alice@example.com}}`

- Exportați cheia privată cu o adresă de e-mail specificată la ieșirea standard:

`gpg2 --export-secret-keys --armor {{alice@example.com}}`
