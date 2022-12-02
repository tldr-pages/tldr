# openssl x509

> OpenSSL command to manage X.509 certificates.
> More information: <https://www.openssl.org/docs/manmaster/man1/openssl-x509.html>.

- Display certificate information:

`openssl x509 -in {{path/to/file.crt}} -noout -text`

- Display a certificate's expiration date:

`openssl x509 -enddate -noout -in {{path/to/file.pem}}`

- Convert a certificate between binary DER encoding and textual PEM encoding:

`openssl x509 -inform {{der}} -outform {{pem}} -in {{path/to/file}} -out {{path/to/file}}`

- Store a certificate's public key in a file:

`openssl x509 -in {{path/to/file}} -noout -pubkey -out {{path/to/file}}`
