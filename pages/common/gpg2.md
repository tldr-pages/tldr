# gpg2

> GNU Privacy Guard 2.
> See `gpg` for GNU Privacy Guard 1.
> More information: <https://docs.releng.linuxfoundation.org/en/latest/gpg.html>.

- List imported keys:

`gpg2 --list-keys`

- Encrypt a specified file for a specified recipient, writing the output to a new file with `.gpg` appended:

`gpg2 --encrypt --recipient {{alice@example.com}} {{path/to/doc.txt}}`

- Encrypt a specified file with only a passphrase, writing the output to a new file with `.gpg` appended:

`gpg2 --symmetric {{path/to/doc.txt}}`

- Decrypt a specified file, writing the result to the standard output:

`gpg2 --decrypt {{path/to/doc.txt.gpg}}`

- Import a public key:

`gpg2 --import {{path/to/public_key.gpg}}`

- Export the public key of a specified email address to the standard output:

`gpg2 --export --armor {{alice@example.com}}`

- Export the private key with a specified email address to the standard output:

`gpg2 --export-secret-keys --armor {{alice@example.com}}`
