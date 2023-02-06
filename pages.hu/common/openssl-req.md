# openssl req

> OpenSSL parancs a PKCS#10 tanúsítvány aláírási kérelmek kezelésére. További információ: <https://www.openssl.org/docs/manmaster/man1/openssl-req.html>.

- Tanúsítvány aláírási kérelem generálása a tanúsítványkiadónak való elküldéshez:

`openssl req -new -sha256 -key {{filename.key}} -out {{filename.csr}}`

- Létrehoz egy saját aláírású tanúsítványt és egy megfelelő kulcspárt, mindkettőt egy fájlban tárolva:

`openssl req -new -x509 -newkey {{rsa}}:{{4096}} -keyout {{filename.key}} -out {{filename.cert}} -subj "{{/C=XX/CN=foobar}}" -days {{365}}`
