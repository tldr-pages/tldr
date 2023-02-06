# serve

> Statikus fájlkiszolgálás és könyvtárlistázás. További információ: <https://github.com/vercel/serve>.

- Indítson el egy HTTP-kiszolgálót, amely az alapértelmezett porton hallgat az aktuális könyvtár kiszolgálására:

`serve`

- HTTP-kiszolgáló indítása egy adott \[p\]orton egy adott könyvtár kiszolgálásához:

`serve -p {{port}} {{path/to/directory}}`

- HTTP-kiszolgáló indítása a CORS engedélyezésével, a `Access-Control-Allow-Origin: *` fejléc minden válaszba történő beépítésével:

`serve --cors`

- HTTP-kiszolgáló indítása az alapértelmezett porton, az összes nem talált kérés átírása a `index.html` fájlba:

`serve --single`

- HTTPS-kiszolgáló indítása az alapértelmezett porton a megadott tanúsítvány használatával:

`serve --ssl-cert {{path/to/cert.pem}} --ssl-key {{path/to/key.pem}}`

- HTTP-kiszolgáló indítása az alapértelmezett porton egy adott konfigurációs fájl használatával:

`serve --config {{path/to/serve.json}}`

- Súgó megjelenítése:

`serve --help`
