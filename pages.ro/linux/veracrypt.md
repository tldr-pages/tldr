# veracrypt

> Software gratuit și open source de criptare disc.
> Mai multe informaţii: <https://www.veracrypt.fr/code/VeraCrypt/plain/doc/html/Documentation.html>

- Creați un volum nou printr-o interfață de utilizator text și utilizați `/dev/urandom` ca sursă de date aleatorii:

`veracrypt --text --create --random-source={{/dev/urandom}}`

- Decripta un volum interactiv printr-o interfață de utilizator text și montați-l într-un director:

`veracrypt --text {{path/to/volume}} {{path/to/mount_point}}`

- Decriptați o partiție utilizând un fișier cheie și montați-o într-un director:

`veracrypt --keyfiles={{path/to/keyfile}} {{/dev/sdXN}} {{path/to/mount_point}}`

- Demontați un volum din directorul în care este montat:

`veracrypt --dismount {{path/to/mounted_point}}`
