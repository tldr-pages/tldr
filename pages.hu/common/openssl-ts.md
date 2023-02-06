# openssl ts

> OpenSSL parancs az időbélyegek létrehozására és ellenőrzésére. További információ: <https://www.openssl.org/docs/manmaster/man1/openssl-ts.html>.

- Egy adott fájl SHA-512 időbélyegző-kérésének generálása és kimenete a `file.tsq` címen:

`openssl ts -query -data {{path/to/file}} -sha512 -out {{path/to/file.tsq}}`

- Ellenőrizze egy adott időbélyeg-válaszfájl dátumát és metaadatait:

`openssl ts -reply -in {{path/to/file.tsr}} -text`

- Ellenőrizzen egy időbélyeg-kérelmi fájlt és egy időbélyeg-válaszfájlt a kiszolgálótól származó SSL-tanúsítványfájllal:

`openssl ts -verify -in {{path/to/file.tsr}} -queryfile {{path/to/file.tsq}} -partial_chain -CAfile {{path/to/cert.pem}}`

- A kulcs és az aláíró tanúsítvány felhasználásával időbélyeg-válaszfájl létrehozása a kérelemhez, és kimenete a `file.tsr` címre:

`openssl ts -reply -queryfile {{path/to/file.tsq}} -inkey {{path/to/tsakey.pem}} -signer tsacert.pem -out {{path/to/file.tsr}}`
