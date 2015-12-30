# openssl

> OpenSSL is a cryptography toolkit.

- Check an SSL connection

`openssl s_client -connect {{url}}:443`

- Generate new private key and CSR

`openssl req -out {{path/to/CSR.csr}} -new -newkey rsa:2048 -nodes -keyout {{path/to/pivate.key}}`

- Read contents of certificate, private key and CSR file

`openssl x509 -text -noout -in {{path/to/certificate.crt}}`
`openssl rsa -check -in {{path/to/pivate.key}}`
`openssl req -text -noout -verify -in {{path/to/CSR.csr}}`

- Check if certificate, private key and CSR have the same MD5 hash

`openssl x509 -noout -modulus -in {{path/to/certificate.crt}} | openssl md5`
`openssl rsa -noout -modulus -in {{path/to/pivate.key}} | openssl md5`
`openssl req -noout -modulus -in {{path/to/CSR.csr}} | openssl md5`
