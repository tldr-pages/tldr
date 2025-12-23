# openssl req

> OpenSSL command to manage PKCS#10 Certificate Signing Requests.
> More information: <https://docs.openssl.org/master/man1/openssl-req/>.

- Generate a certificate signing request to be sent to a certificate authority:

`openssl req -new -sha256 -key {{filename.key}} -out {{filename.csr}}`

- Generate a self-signed certificate and a corresponding key-pair, storing both in a file:

`openssl req -new -x509 -newkey {{rsa}}:{{4096}} -keyout {{filename.key}} -out {{filename.cert}} -subj "{{/C=XX/CN=foobar}}" -days {{365}}`
