# openssl x509

> OpenSSL command to manage X.509 certificates.
> More information: <https://www.openssl.org/docs/manmaster/man1/openssl-x509.html>.

- Generate a self-signed certificate from a certificate signing request valid for some number of days:

`openssl x509 -req -days {{days}} -in {{filename.csr}} -signkey {{filename.key}} -out {{filename.crt}}`

- Display certificate information:

`openssl x509 -in {{filename.crt}} -noout -text`

- Display a certificate's expiration date:

`openssl x509 -enddate -noout -in {{filename.pem}}`
