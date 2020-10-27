# openssl dgst

> OpenSSL command to generate digest values and perform signature operations.
> More information: <https://www.openssl.org/docs/man1.0.2/man1/dgst.html>.

- Generate a SHA256 hash value of a file:

`openssl dgst -sha256 -binary -out {{output_file}} {{input_file}}`

- Sign a file using and RSA key:

`openssl dgst -sign {{private_key_file}} -sha256 -sigopt rsa_padding_mode:pss -out {{output_file}} {{input_file}}`

- Verify an RSA signature:

`openssl dgst -verify {{public_key_file}} -signature {{signature_file}} -sigopt rsa_padding_mode:pss {{signature_message_file}}`

- Sign a file using and ECDSA key:

`openssl dgst -sign {{private_key_file}} -sha256 -out {{output_file}} {{input_file}}`

- Verify an ECDSA signature:

`openssl dgst -verify {{public_key_file}} -signature {{signature_file}} {{signature_message_file}}`
