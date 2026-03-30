# openssl req

> Gestiona Solicitudes de Firma de Certificado (CSR) PKCS#10.
> Más información: <https://docs.openssl.org/master/man1/openssl-req/>.

- Genera una solicitud de firma de certificado para enviar a una autoridad certificadora:

`openssl req -new -sha256 -key {{nombre_archivo.key}} -out {{nombre_archivo.csr}}`

- Genera un certificado autofirmado y su par de claves correspondiente, almacenando ambos en un archivo:

`openssl req -new -x509 -newkey {{rsa}}:{{4096}} -keyout {{nombre_archivo.key}} -out {{nombre_archivo.cert}} -subj "{{/C=XX/CN=foobar}}" -days {{365}}`
