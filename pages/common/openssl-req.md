# openssl req

> OpenSSL command to manage PKCS#10 Certificate Signing Requests.
> More information: <https://www.openssl.org/docs/manmaster/man1/openssl-req.html>.

- Generate a certificate signing request to be sent to a certificate authority:

`openssl req -new -sha256 -key {{path/to/file.key}} -out {{path/to/file.csr}}`

- Generate a self-signed certificate and a corresponding key-pair, storing both in a file:

`openssl req -new -x509 -newkey {{rsa}}:{{4096}} -keyout {{path/to/file.key}} -out {{path/to/file.cert}} -subj "{{/C=XX/CN=foobar}}" -days {{365}}`
