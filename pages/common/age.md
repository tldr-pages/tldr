# age

> A simple, modern and secure file encryption tool.
> See also: `age-keygen` for generating key pairs.
> More information: <https://github.com/FiloSottile/age#usage>.

- Generate an encrypted file that can be decrypted with a passphrase:

`age {{[-p|--passphrase]}} {{[-o|--output]}} {{path/to/encrypted_file}} {{path/to/unencrypted_file}}`

- Encrypt a file with one or more public keys entered as literals (repeat the `--recipient` flag to specify multiple public keys):

`age {{[-r|--recipient]}} {{public_key}} {{[-o|--output]}} {{path/to/encrypted_file}} {{path/to/unencrypted_file}}`

- Encrypt a file to one or more recipients with their public keys specified in a file (one per line):

`age {{[-R|--recipients-file]}} {{path/to/recipients_file}} {{[-o|--output]}} {{path/to/encrypted_file}} {{path/to/unencrypted_file}}`

- Decrypt a file with a passphrase:

`age {{[-d|--decrypt]}} {{[-o|--output]}} {{path/to/decrypted_file}} {{path/to/encrypted_file}}`

- Decrypt a file with a private key file:

`age {{[-d|--decrypt]}} {{[-i|--identity]}} {{path/to/private_key_file}} {{[-o|--output]}} {{path/to/decrypted_file}} {{path/to/encrypted_file}}`
