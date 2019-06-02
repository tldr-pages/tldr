# gpg

> GNU Privacy Guard 2.
> Homepage: <https://docs.releng.linuxfoundation.org/en/latest/gpg.html>.

- List imported keys:

`gpg2 --list-keys`

- Encrypt doc.txt for alice@example.com (output to doc.txt.gpg):

`gpg2 --encrypt --recipient {{alice@example.com}} {{doc.txt}}`

- Encrypt doc.txt with only a passphrase (output to doc.txt.gpg):

`gpg2 --symmetric {{doc.txt}}`

- Decrypt doc.txt.gpg (output to STDOUT):

`gpg2 --decrypt {{doc.txt.gpg}}`

- Import a public key:

`gpg2 --import {{public.gpg}}`

- Export public key for alice@example.com (output to STDOUT):

`gpg2 --export --armor {{alice@example.com}}`

- Export private key for alice@example.com (output to STDOUT):

`gpg2 --export-secret-keys --armor {{alice@example.com}}`
