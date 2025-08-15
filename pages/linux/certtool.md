# certtool

> Generate and manage X.509 certificates, keys, and PKI structures using GnuTLS.
> More information: <https://gnutls.org/manual/gnutls.html#certtool-Invocation>.

- Generate a private key and save it to a file:

`certtool {{[-p|--generate-privkey]}} --outfile {{path/to/private.key}}`

- Generate a self-signed certificate using a private key and a template file:

`certtool {{[-s|--generate-self-signed]}} --load-privkey {{path/to/private.key}} --template {{path/to/info.template}} --outfile {{path/to/certificate.crt}}`

- Generate a certificate signing request (CSR):

`certtool {{[-q|--generate-request]}} --load-privkey {{path/to/private.key}} --template {{path/to/info.template}} --outfile {{path/to/request.csr}}`

- Generate a certificate authority (CA) certificate:

`certtool {{[-s|--generate-self-signed]}} --load-privkey {{path/to/ca.key}} --template {{path/to/ca.template}} --outfile {{path/to/ca.crt}}`

- Verify a certificate against a CA certificate:

`certtool --verify --infile {{path/to/certificate.crt}} --load-ca-certificate {{path/to/ca.crt}}`
