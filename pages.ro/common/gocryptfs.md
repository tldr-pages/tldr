# gocryptfs

> Sisteme de fișiere suprapuse criptate scrise în Go.
> Mai multe informaţii: <https://github.com/rfjakob/gocryptfs>

- Iniţializează un sistem de fişiere criptat:

`gocryptfs -init {{path/to/cipher_dir}}`

- Montați un sistem de fișiere criptat:

`gocryptfs {{path/to/cipher_dir}} {{path/to/mount_point}}`

- Montați cu cheia principală explicită în loc de parolă:

`gocryptfs --masterkey {{path/to/cipher_dir}} {{path/to/mount_point}}`

- Schimbă parola:

`gocryptfs --passwd {{path/to/cipher_dir}}`

- Faceți un instantaneu criptat al unui director simplu:

`gocryptfs --reverse {{path/to/plain_dir}} {{path/to/cipher_dir}}`
