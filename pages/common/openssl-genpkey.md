# openssl genpkey

> OpenSSL command to generate asymmetric key pairs.
> More information: <https://www.openssl.org/docs/man1.0.2/man1/genpkey.html>.

- Generate a 2048bit RSA private key and save it to a file:

`openssl genpkey -algorithm rsa -pkeyopt rsa_keygen_bits:2048 -out {{filename.key}}`

- Generate an elliptic curve private key using the curve *prime256v1* and save it to a file:

`openssl genpkey -algorithm EC -pkeyopt ec_paramgen_curve:prime256v1 -out {{filename.key}}`

- Generate an ED25519 elliptic curve private key and save it to a file:

`openssl genpkey -algorithm ED25519 -out {{filename.key}}`
