# openssl req

> comanda OpenSSL pentru a gestiona solicitările de semnare a certificatelor PKCS #10.
> Mai multe informaţii: <https://www.openssl.org/docs/manmaster/man1/openssl-req.html>

- Generarea unei cereri de semnare a certificatului care urmează să fie trimisă unei autorități de certificare

`openssl req -new -sha256 -key {{filename.key}} -out {{filename.csr}}`

- Generați un certificat autosemnat și o pereche de chei corespunzătoare, stocând ambele într-un fișier:

`openssl req -new -x509 -newkey {{rsa}}:{{4096}} -keyout {{filename.key}} -out {{filename.cert}} -subj "{{/C=XX/CN=foobar}}" -days {{365}}`
