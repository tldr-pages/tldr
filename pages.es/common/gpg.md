# gpg

> GNU Privacy Guard, una herramienta de cifrado y firma OpenPGP.
> Más información: <https://gnupg.org/documentation/manuals/gnupg/Invoking-GPG.html>.

- Crea una clave pública y privada GPG de forma interactiva:

`gpg {{[--full-gen-key|--full-generate-key]}}`

- Lista todas las claves del llavero público:

`gpg {{[-k|--list-keys]}}`

- Firma `doc.txt` sin cifrar (escribe el resultado en `doc.txt.asc`):

`gpg --clearsign {{doc.txt}}`

- Cifra y firma `doc.txt` para `alice@example.com` y `bob@example.com` (salida a `doc.txt.gpg`):

`gpg {{[-es|--encrypt --sign]}} {{[-r|--recipient]}} {{alice@example.com}} {{[-r|--recipiente]}} {{bob@example.com}} {{doc.txt}}`

- Cifra `doc.txt` con solo una frase de contraseña (salida a `doc.txt.gpg`):

`gpg {{[-c|---symmetric]}} {{doc.txt}}`

- Descifra `doc.txt.gpg` (salida a `stdout`):

`gpg {{[-d|--decrypt]}} {{doc.txt.gpg}}`

- Importa una clave pública:

`gpg --import {{public.gpg}}`

- Exporta la clave pública/privada para `alice@example.com` (salida a `stdout`):

`gpg {{--export|--export-secret-keys}} {{[-a|--armor]}} {{alice@example.com}}`
