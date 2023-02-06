# cockpit-ws

> Kommunikáció a böngészőalkalmazás és a különböző konfigurációs eszközök és szolgáltatások között, mint például a `cockpit-bridge`. További információ: [https://cockpit-project.org/guide/latest/cockpit-ws.8.html.](https://cockpit-project.org/guide/latest/cockpit-ws.8.html)

- Kezdje a hitelesítéssel SSH-n keresztül a `127.0.0.1` címen, a `22` port engedélyezésével:

`cockpit-ws --local-ssh`

- HTTP-kiszolgáló indítása egy adott porton:

`cockpit-ws --port {{port}}`

- Indítsa el és kösse le egy adott IP-címhez (alapértelmezés szerint a `0.0.0.0`):

`cockpit-ws --address {{ip_address}}`

- TLS nélküli indítás:

`cockpit-ws --no-tls`

- Súgó megjelenítése:

`cockpit-ws --help`
