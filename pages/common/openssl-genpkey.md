# openssl genpkey

> OpenSSL command to generate asymmetric key pairs.
> More information: <https://docs.openssl.org/master/man1/openssl-genpkey/>.

- Generate an RSA private key of 2048 bits, saving it to a specific file:

`openssl genpkey -algorithm rsa -pkeyopt rsa_keygen_bits:{{2048}} -out {{path/to/private.key}}`

- Generate an elliptic curve private key using the curve `prime256v1`, saving it to a specific file:

`openssl genpkey -algorithm EC -pkeyopt ec_paramgen_curve:{{prime256v1}} -out {{path/to/private.key}}`

- Generate an `ED25519` elliptic curve private key, saving it to a specific file:

`openssl genpkey -algorithm {{ED25519}} -out {{path/to/private.key}}`
