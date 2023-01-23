# openssl genpkey

> OpenSSL parancs aszimmetrikus kulcspárok létrehozására. További információ: <https://www.openssl.org/docs/manmaster/man1/openssl-genpkey.html>.

- Generáljon egy 2048 bites RSA magánkulcsot, és mentse el egy adott fájlba:

`openssl genpkey -algorithm rsa -pkeyopt rsa_keygen_bits:{{2048}} -out {{filename.key}}`

- Elliptikus görbe magánkulcs generálása a `prime256v1` görbe segítségével, mentve egy adott fájlba:

`openssl genpkey -algorithm EC -pkeyopt ec_paramgen_curve:{{prime256v1}} -out {{filename.key}}`

- Egy `ED25519` elliptikus görbe magánkulcs generálása, mentése egy adott fájlba:

`openssl genpkey -algorithm {{ED25519}} -out {{filename.key}}`
