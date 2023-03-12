# dropbearkey

> Generate SSH keys in Dropbear format.
> More information: <https://manned.org/dropbearkey.1>.

- Generate a SSH key of [t]ype ed25519 and write it to key [f]ile:

`dropbearkey -t {{ed25519}} -f {{path/to/key}}`

- Generate a SSH key of [t]ype ecdsa and write it to key [f]ile:

`dropbearkey -t {{ecdsa}} -f {{path/to/key}}`

- Generate a SSH key of [t]ype RSA with 4096-bit key [s]ize and write it to key [f]ile:

`dropbearkey -t {{rsa}} -s {{4096}} -f {{path/to/key}}`

- Print the private key fingerprint and public key in key [f]ile:

`dropbearkey -y -f {{pay/to/key}}`
