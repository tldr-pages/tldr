# age-keygen

> Generate `age` key pairs.
> See also: `age`, `age-inspect`.
> More information: <https://manned.org/age-keygen>.

- Generate a key pair, save it to an unencrypted file, and print the public key to `stdout`:

`age-keygen {{[-o|--output]}} {{path/to/file}}`

- Generate a post-quantum key pair, save it to an unencrypted file, and print the public key to `stdout`:

`age-keygen -pq {{[-o|--output]}} {{path/to/file}}`

- Convert an identit[y] to a recipient and print the public key to `stdout`:

`age-keygen -y {{path/to/file}}`
