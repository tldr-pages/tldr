# openssl

> OpenSSL cryptographic toolkit.
> Some subcommands such as `req` have their own usage documentation.
> More information: <https://www.openssl.org>.

- Display version:

`openssl version`

- Generate an encrypted private key:

`openssl genpkey -algorithm {{[RSA|EC]}} -out {{private.key}} -aes256`

- Generate the corresponding public key from private key `private.key`:

`openssl {{[rsa|ec]}} -in {{private.key}} -pubout -out {{public.key}}`

- Generate a self-signed certificate valid for a specified number of days (`365`):

`openssl req -new -x509 -key {{private.key}} -out {{certificate.crt}} -days {{365}}`

- Convert certificate to PEM or DER format:

`openssl x509 -in {{certificate.crt}} -out {{[certificate.pem|certificate.der]}} -outform {{[PEM|DER]}}`

- Check certificate details:

`openssl x509 -in {{certificate.crt}} -text -noout`

- Generate a certificate signing request (CSR):

`openssl req -new -key {{private.key}} -out {{request.csr}}`
