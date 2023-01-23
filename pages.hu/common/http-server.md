# http-server

> Egyszerű statikus HTTP-kiszolgáló statikus fájlok kiszolgálására. További információ: <https://github.com/http-party/http-server>.

- HTTP-kiszolgáló indítása az alapértelmezett porton az aktuális könyvtár kiszolgálására:

`http-server`

- HTTP-kiszolgáló indítása egy adott porton egy adott könyvtár kiszolgálásához:

`http-server {{path/to/directory}} --port {{port}}`

- HTTP-kiszolgáló indítása alapvető hitelesítéssel:

`http-server --username {{username}} --password {{password}}`

- HTTP-kiszolgáló indítása a könyvtárak listázásának letiltásával:

`http-server -d {{false}}`

- HTTPS-kiszolgáló indítása az alapértelmezett porton a megadott tanúsítvány használatával:

`http-server --ssl --cert {{path/to/cert.pem}} --key {{path/to/key.pem}}`

- HTTP-kiszolgáló indítása és az ügyfél IP-címének feltüntetése a kimeneti naplózásban:

`http-server --log-ip`

- HTTP-kiszolgáló indítása a CORS engedélyezésével, a `Access-Control-Allow-Origin: *` fejlécet minden válaszba beépítve:

`http-server --cors`

- HTTP-kiszolgáló indítása naplózás letiltásával:

`http-server --silent`
