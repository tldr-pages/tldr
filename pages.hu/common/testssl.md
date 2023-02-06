# testssl

> Ellenőrizze a kiszolgáló által támogatott SSL/TLS protokollokat és titkosításokat. További információ: <https://testssl.sh/>.

- Teszteljen egy kiszolgálót (futtasson le minden ellenőrzést) a 443-as porton:

`testssl {{example.com}}`

- Teszteljen egy másik portot:

`testssl {{example.com:465}}`

- Csak az elérhető protokollokat ellenőrizze:

`testssl --protocols {{example.com}}`

- Csak a sebezhetőségeket ellenőrizze:

`testssl --vulnerable {{example.com}}`

- Csak a HTTP biztonsági fejlécek ellenőrzése:

`testssl --headers {{example.com}}`
