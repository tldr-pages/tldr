# openssl

> OpenSSL cryptographic toolkit.

- Generate a 2048bit RSA private key and save it to a file:

`openssl genrsa -out {{filename.key}} 2048`

- Generate a certificate signing request to be sent to a certificate authority:

`openssl req -new -sha256 -key {{filename.key}} -out {{filename.csr}}`

- Read contents of a signed certificate:

`openssl x509 -text -noout -in {{certificate.crt}}`

- Display the certificate presented by an SSL/TLS server:

`openssl s_client -connect {{host}}:{{port}} </dev/null`

- Display the complete certificate chain of an HTTPS server:

`openssl s_client -connect {{google.com}}:{{443}} -showcerts </dev/null`
