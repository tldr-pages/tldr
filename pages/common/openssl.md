# openssl

> OpenSSL cryptographic toolkit.
> Some subcommands such as `req` have their own usage documentation.
> More information: <https://docs.openssl.org/master/man1/openssl/>.

- Generate a private key and encrypt the output file using AES-256:

`openssl genpkey -algorithm {{rsa|ec}} -out {{path/to/private.key}} -aes256`

- Generate the corresponding public key from the private key `private.key` using `rsa`:

`openssl rsa -in {{path/to/private.key}} -pubout -out {{path/to/public.key}}`

- Generate a self-signed certificate valid for a specified number of days (365):

`openssl req -new -x509 -key {{path/to/private.key}} -out {{path/to/certificate.crt}} -days 365`

- Convert a certificate to `.pem` or `.der` format:

`openssl x509 -in {{path/to/certificate.crt}} -out {{path/to/certificate.pem|path/to/certificate.der}} -outform {{pem|der}}`

- Check certificate details:

`openssl x509 -in {{path/to/certificate.crt}} -text -noout`

- Generate a certificate signing request (CSR):

`openssl req -new -key {{path/to/private.key}} -out {{path/to/request.csr}}`

- Display help:

`openssl help`

- Display version:

`openssl version`
