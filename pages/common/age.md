# age

> A simple, modern and secure file encryption tool.
> More information: <https://age-encryption.org>.

- Generate an encrypted file that can be decrypted with a passphrase:

`age --passphrase --output {{path/to/encrypted_file}} {{path/to/unencrypted_file}}`

- Generate a keypair, saving the private key and the public key to an unencrypted keyfile and printing the public key to stdout:

`age-keygen --output {{path/to/keyfile}}`

- Encrypt a file to one or several public keys that are entered as literals:

`age --output {{path/to/encrypted_file}} --recipient {{publickey1}} --recipient {{publickey2}} {{path/to/unencrypted_file}}`

- Encrypt a file to one or several public keys that are specified in a recipients file:

`age --output {{path/to/encrypted_file}} --recipients-file {{path/to/recipients_file}} {{path/to/unencrypted_file}}`

- Decrypt a file with a passphrase:

`age --decrypt --output {{path/to/decrypted_file}} {{path/to/encrypted_file}}`

- Decrypt a file with a private keyfile:

`age --decrypt --identity {{path/to/private_keyfile}} --output {{path/to/decrypted_file}} {{path/to/encrypted_file}}`
