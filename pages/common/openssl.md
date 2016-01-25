# openssl

> OpenSSL is a cryptography toolkit.

- Check an SSL connection:

`openssl s_client -connect {{domain}}:{{port}}`

- Generate new private key and CSR:

`openssl req -out {{path/to/CSR.csr}} -new -newkey rsa:2048 -nodes -keyout {{path/to/pivate.key}}`

- Read contents of a certificate:

`openssl x509 -text -noout -in {{path/to/certificate.crt}}`

- Read contents of a private key:

`openssl rsa -check -in {{path/to/pivate.key}}`

- Verify a CSR file:

`openssl req -text -noout -verify -in {{path/to/CSR.csr}}`

- Check MD5 hash of a certificate:

`openssl x509 -noout -modulus -in {{path/to/certificate.crt}} | openssl md5`

- Check MD5 hash of a private key:

`openssl rsa -noout -modulus -in {{path/to/pivate.key}} | openssl md5`

- Check MD5 hash of a CSR file:

`openssl req -noout -modulus -in {{path/to/CSR.csr}} | openssl md5`
