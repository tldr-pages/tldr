# openssl prime

> OpenSSL parancs prímszámok kiszámítására. További információ: <https://www.openssl.org/docs/manmaster/man1/openssl-prime.html>.

- Generáljon egy 2048 bites prímszámot, és jelenítse meg hexadecimálisan:

`openssl prime -generate -bits 2048 -hex`

- Ellenőrizze, hogy egy adott szám prím-e:

`openssl prime {{number}}`
