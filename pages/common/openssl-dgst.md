# openssl dgst

> OpenSSL command to generate digest values and perform signature operations.
> More information: <https://www.openssl.org/docs/manmaster/man1/openssl-dgst.html>.

- Calculate the SHA256 digest for a file, saving the result to a specific file:

`openssl dgst -sha256 -binary -out {{path/to/file}} {{path/to/file}}`

- Sign a file using an RSA key, saving the result to a specific file:

`openssl dgst -sign {{path/to/file}} -sha256 -sigopt rsa_padding_mode:pss -out {{path/to/file}} {{path/to/file}}`

- Verify an RSA signature:

`openssl dgst -verify {{path/to/file}} -signature {{path/to/file}} -sigopt rsa_padding_mode:pss {{path/to/file}}`

- Sign a file using and ECDSA key:

`openssl dgst -sign {{path/to/file}} -sha256 -out {{path/to/file}} {{path/to/file}}`

- Verify an ECDSA signature:

`openssl dgst -verify {{path/to/file}} -signature {{path/to/file}} {{path/to/file}}`
