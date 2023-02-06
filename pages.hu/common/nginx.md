# nginx

> Nginx webszerver. További információ: <https://nginx.org/en/>.

- Indítsa el a kiszolgálót az alapértelmezett konfigurációs fájllal:

`nginx`

- Kiszolgáló indítása egyéni konfigurációs fájllal:

`nginx -c {{configuration_file}}`

- Kiszolgáló indítása a konfigurációs fájlban lévő összes relatív elérési útvonal előtaggal:

`nginx -c {{configuration_file}} -p {{prefix/for/relative/paths}}`

- A konfiguráció tesztelése a futó kiszolgáló befolyásolása nélkül:

`nginx -t`

- A konfiguráció újratöltése egy jel elküldésével, leállási idő nélkül:

`nginx -s reload`
