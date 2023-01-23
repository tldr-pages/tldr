# caddy

> Go nyelven írt, vállalati szintű nyílt forráskódú webszerver automatikus HTTPS-sel. További információ: <https://caddyserver.com>.

- Indítsa el a Caddy-t az előtérben:

`caddy run`

- A Caddy elindítása a megadott Caddyfillel:

`caddy run --config {{path/to/Caddyfile}}`

- A Caddy elindítása a háttérben:

`caddy start`

- A háttérben futó Caddy folyamat leállítása:

`caddy stop`

- Egy egyszerű fájlszerver futtatása a megadott porton, böngészhető felülettel:

`caddy file-server --listen :{{8000}} --browse`

- Fordított proxy-kiszolgáló futtatása:

`caddy reverse-proxy --from :{{80}} --to localhost:{{8000}}`
