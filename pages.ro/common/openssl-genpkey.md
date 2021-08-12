# openssl genpkey

> comanda OpenSSL pentru a genera perechi de taste asimetrice.
> Mai multe informaţii: <https://www.openssl.org/docs/manmaster/man1/openssl-genpkey.html>

- Generați o cheie privată RSA de 2048 biți, salvând-o într-un anumit fișier:

`openssl genpkey -algorithm rsa -pkeyopt rsa_keygen_bits:{{2048}} -out {{filename.key}}`

- Generați o cheie privată cu curbă eliptică utilizând curba `prime256v1`, salvând-o într-un anumit fișier:

`openssl genpkey -algorithm EC -pkeyopt ec_paramgen_curve:{{prime256v1}} -out {{filename.key}}`

- Generați o cheie privată cu curbă eliptică `ED25519`, salvând-o într-un anumit fișier:

`openssl genpkey -algorithm {{ED25519}} -out {{filename.key}}`
