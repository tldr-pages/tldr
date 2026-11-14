# botan

> Provide cryptographic operations including hashing, encryption, and key generation.
> More information: <https://botan.randombit.net/handbook/cli.html>.

- Compute the digest of a file with a specific algorithm:

`botan hash --algo={{SHA-256}} {{path/to/file}}`

- Encode a file to Base64:

`botan base64_enc {{path/to/file}}`

- Encrypt a file with AES-256/GCM (key and nonce are hex-encoded):

`botan cipher --cipher=AES-256/GCM --key={{hex_key}} --nonce={{hex_nonce}} --output={{path/to/output_file}} {{path/to/file}}`

- Decrypt a file with AES-256/GCM:

`botan cipher --cipher=AES-256/GCM --decrypt --key={{hex_key}} --nonce={{hex_nonce}} --output={{path/to/output_file}} {{path/to/file}}`

- Generate an RSA private key:

`botan keygen --algo=RSA --params=2048 >{{path/to/private_key.pem}}`

- Print 16 random bytes:

`botan rng 16`

- Display help:

`botan --help`

- Display version:

`botan version`
