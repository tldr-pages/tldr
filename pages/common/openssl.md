# openssl

> OpenSSL command line toolkit.

- Generate a 2048bit RSA private key and save it to a file:

`openssl genrsa -out {{filename.key}} 2048`

- Generate a certificate signing request to be sent to a certificate authority:

`openssl req -new -sha256 -key {{filename.key}} -out {{filename.csr}}`

- Display contents of a certificate signing request:

`openssl req -in {{filename.csr}} -noout -text`

- Display the server certificate of an SSL/TLS server:

`openssl s_client -connect {{host_name}}:{{port}} </dev/null`

- Display the complete certificate chain of an HTTPS server:

`openssl s_client -connect {{google.com}}:{{443}} -showcerts </dev/null`
