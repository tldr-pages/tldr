# gocryptfs

> Go nyelven írt titkosított overlay fájlrendszer. További információ: <https://github.com/rfjakob/gocryptfs>.

- Titkosított fájlrendszer inicializálása:

`gocryptfs -init {{path/to/cipher_dir}}`

- Titkosított fájlrendszer csatlakoztatása:

`gocryptfs {{path/to/cipher_dir}} {{path/to/mount_point}}`

- Mount a jelszó helyett explicit mester kulccsal:

`gocryptfs --masterkey {{path/to/cipher_dir}} {{path/to/mount_point}}`

- Jelszó módosítása:

`gocryptfs --passwd {{path/to/cipher_dir}}`

- Titkosított pillanatkép készítése egy sima könyvtárról:

`gocryptfs --reverse {{path/to/plain_dir}} {{path/to/cipher_dir}}`
