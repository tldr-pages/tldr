# age-keygen

> Generate `age` key pairs.
> See `age` for how to encrypt/decrypt files.
> More information: <https://manned.org/age-keygen>.

- Generate a key pair, save it to an unencrypted file and print the public key to `stdout`:

`age-keygen --output {{path/to/file}}`

- Convert an identity to a recipient and print the public key to `stdout`:

`age-keygen -y {{path/to/file}}`
