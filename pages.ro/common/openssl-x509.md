# openssl x509

> comanda OpenSSL pentru gestionarea certificatelor X.509.
> Mai multe informaţii: <https://www.openssl.org/docs/manmaster/man1/openssl-x509.html>

- Afișează informații despre certificat:

`openssl x509 -in {{filename.crt}} -noout -text`

- Afișează data de expirare a certificatului:

`openssl x509 -enddate -noout -in {{filename.pem}}`

- Conversia unui certificat între codificarea binară DER și codificarea PEM textuală:

`openssl x509 -inform {{der}} -outform {{pem}} -in {{original_certificate_file}} -out {{converted_certificate_file}}`

- Stocați cheia publică a unui certificat într-un fișier:

`openssl x509 -in {{certificate_file}} -noout -pubkey -out {{output_file}}`
