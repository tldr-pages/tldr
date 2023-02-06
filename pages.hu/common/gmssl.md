# gmssl

> A GmSSL egy kripto eszközkészlet, amely támogatja az SM1, SM2, SM3, SM4, SM9 és ZUC/ZUC256 titkosításokat. További információ: <http://gmssl.org/english.html>.

- SM3 hash generálása egy fájlhoz:

`gmssl sm3 {{path/to/file}}`

- Egy fájl titkosítása SM4 titkosítással:

`gmssl sms4 -e -in {{path/to/file}} -out {{path/to/file.sms4}}`

- Fájl visszafejtése SM4 titkosítással:

`gmssl sms4 -d -in {{path/to/file.sms4}}`

- SM2 privát kulcs generálása:

`gmssl sm2 -genkey -out {{path/to/file.pem}}`

- SM2 nyilvános kulcs generálása egy meglévő magánkulcsból:

`gmssl sm2 -pubout -in {{path/to/file.pem}} -out {{path/to/file.pem.pub}}`

- Egy fájl titkosítása ZUC titkosítással:

`gmssl zuc -e -in {{path/to/file}} -out {{path/to/file.zuc}}`

- Fájl visszafejtése a ZUC titkosítással:

`gmssl zuc -d -in {{path/to/file.zuc}}`

- Nyomtatási verzió:

`gmssl version`
