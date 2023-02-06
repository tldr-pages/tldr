# openssl x509

> OpenSSL parancs az X.509 tanúsítványok kezelésére. További információ: <https://www.openssl.org/docs/manmaster/man1/openssl-x509.html>.

- Tanúsítványinformációk megjelenítése:

`openssl x509 -in {{filename.crt}} -noout -text`

- A tanúsítvány lejárati dátumának megjelenítése:

`openssl x509 -enddate -noout -in {{filename.pem}}`

- Tanúsítvány átalakítása bináris DER-kódolás és szöveges PEM-kódolás között:

`openssl x509 -inform {{der}} -outform {{pem}} -in {{original_certificate_file}} -out {{converted_certificate_file}}`

- A tanúsítvány nyilvános kulcsának tárolása egy fájlban:

`openssl x509 -in {{certificate_file}} -noout -pubkey -out {{output_file}}`
