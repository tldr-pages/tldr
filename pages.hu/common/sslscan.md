# sslscan

> Ellenőrizze a kiszolgáló által támogatott SSL/TLS protokollokat és titkosításokat. További információ: <https://github.com/rbsec/sslscan>.

- Teszteljen egy kiszolgálót a 443-as porton:

`sslscan {{example.com}}`

- Egy megadott port tesztelése:

`sslscan {{example.com}}:{{465}}`

- Tanúsítványinformációk megjelenítése:

`testssl --show-certificate {{example.com}}`
