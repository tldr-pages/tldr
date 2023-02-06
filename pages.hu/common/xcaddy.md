# xcaddy

> A Caddy Web Server egyedi építőeszköze. További információ: <https://github.com/caddyserver/xcaddy>.

- Caddy szerver építése forrásból:

`xcaddy build`

- Caddy kiszolgáló építése egy adott verzióval (alapértelmezett a legújabb):

`xcaddy build {{version}}`

- Caddy építése egy adott modullal:

`xcaddy build --with {{module_name}}`

- Caddy építése és kimenet egy adott fájlba:

`xcaddy build --output {{path/to/file}}`

- Caddy építése és futtatása az aktuális könyvtárban lévő fejlesztői bővítményhez:

`xcaddy run`

- Caddy építése és futtatása egy fejlesztői bővítményhez egy adott Caddy-konfigurációval:

`xcaddy run --config {{path/to/file}}`
