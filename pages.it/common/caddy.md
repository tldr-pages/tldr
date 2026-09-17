# caddy

> Server web open source enterprise-ready con HTTPS automatico, scritto in Go.
> Maggiori informazioni: <https://caddyserver.com/docs/command-line>.

- Avvia Caddy in primo piano:

`caddy run`

- Avvia Caddy con il Caddyfile specificato:

`caddy run --config {{percorso/del/Caddyfile}}`

- Avvia Caddy in background:

`caddy start`

- Ferma un processo Caddy in background:

`caddy stop`

- Esegue un semplice file server sulla porta specificata con interfaccia navigabile:

`caddy file-server --listen :{{8000}} --browse`

- Esegue un server reverse proxy:

`caddy reverse-proxy --from :{{80}} --to localhost:{{8000}}`
