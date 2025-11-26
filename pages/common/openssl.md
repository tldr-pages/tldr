# openssl

> OpenSSL cryptographic toolkit.
> Some subcommands such as `req` have their own usage documentation.
> More information: <https://www.openssl.org>.

- Generate a private key and encrypt the output file using AES256:

`openssl genpkey -algorithm {{rsa|ec}} -out {{private.key}} -aes256`

- Generate the corresponding public key from private key `private.key` using `rsa`:

`openssl rsa -in {{private.key}} -pubout -out {{public.key}}`

- Generate a self-signed certificate valid for a specified number of days (`365`):

`openssl req -new -x509 -key {{private.key}} -out {{certificate.crt}} -days {{365}}`

- Convert certificate to `pem` or `der` format:

`openssl x509 -in {{certificate.crt}} -out {{certificate.pem|certificate.der}} -outform {{pem|der}}`

- Check certificate details:

`openssl x509 -in {{certificate.crt}} -text -noout`

- Generate a certificate signing request (CSR):

`openssl req -new -key {{private.key}} -out {{request.csr}}`

- Display help:

`openssl help`

- Display version:

`openssl version`
