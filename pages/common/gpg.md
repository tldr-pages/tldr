# gpg

> GNU Privacy Guard, an OpenPGP encryption and signing tool.
> More information: <https://gnupg.org/documentation/manuals/gnupg/Invoking-GPG.html>.

- Create a GPG public and private key interactively:

`gpg {{[--full-gen-key|--full-generate-key]}}`

- List all keys from the public keyring:

`gpg {{[-k|--list-keys]}}`

- Sign `doc.txt` without encryption (writes output to `doc.txt.asc`):

`gpg --clearsign {{doc.txt}}`

- Encrypt and sign `doc.txt` for `alice@example.com` and `bob@example.com` (output to `doc.txt.gpg`):

`gpg {{[-es|--encrypt --sign]}} {{[-r|--recipient]}} {{alice@example.com}} {{[-r|--recipient]}} {{bob@example.com}} {{doc.txt}}`

- Encrypt `doc.txt` with only a passphrase (output to `doc.txt.gpg`):

`gpg {{[-c|--symmetric]}} {{doc.txt}}`

- Decrypt `doc.txt.gpg` (output to `stdout`):

`gpg {{[-d|--decrypt]}} {{doc.txt.gpg}}`

- Import a public key:

`gpg --import {{public.gpg}}`

- Export the public/private key for `alice@example.com` (output to `stdout`):

`gpg {{--export|--export-secret-keys}} {{[-a|--armor]}} {{alice@example.com}}`
