# age

> A simple, modern and secure file encryption tool.
> More information: <https://age-encryption.org>.

- Generate an encrypted file that can be decrypted with a passphrase:

`age --passphrase --output {{path/to/encrypted_file}} {{path/to/unencrypted_file}}`

- Generate a key pair, saving the private key to an unencrypted file and printing the public key to `stdout`:

`age-keygen --output {{path/to/file}}`

- Encrypt a file with one or more public keys that are entered as literals:

`age --recipient {{public_key_1}} --recipient {{public_key_2}} {{path/to/unencrypted_file}} --output {{path/to/encrypted_file}}`

- Encrypt a file with one or more public keys that are specified in a recipients file:

`age --recipients-file {{path/to/recipients_file}} {{path/to/unencrypted_file}} --output {{path/to/encrypted_file}}`

- Decrypt a file with a passphrase:

`age --decrypt --output {{path/to/decrypted_file}} {{path/to/encrypted_file}}`

- Decrypt a file with a private key file:

`age --decrypt --identity {{path/to/private_key_file}} --output {{path/to/decrypted_file}} {{path/to/encrypted_file}}`
