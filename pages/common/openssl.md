# openssl

> OpenSSL is a cryptography toolkit.

- Check an SSL connection

`openssl s_client -connect www.paypal.com:443`

- Generate new private key and CSR

`openssl req -out CSR.csr -new -newkey rsa:2048 -nodes -keyout privateKey.key`

- Read contents of certificate, private key and CSR file

`openssl x509 -text -noout -in certificate.crt`
`openssl rsa -check -in privateKey.key`
`openssl req -text -noout -verify -in CSR.csr`

- Check if certificate, private key and CSR have the same MD5 hash

`openssl x509 -noout -modulus -in certificate.crt | openssl md5`
`openssl rsa -noout -modulus -in privateKey.key | openssl md5`
`openssl req -noout -modulus -in CSR.csr | openssl md5`
