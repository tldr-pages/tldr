# caddy

> Ein unternehmenstauglicher Open-Source-Webserver mit automatischem HTTPS, geschrieben in Go.
> Weitere Informationen: <https://caddyserver.com>.

- Starte Caddy im Vordergrund:

`caddy run`

- Starte Caddy mit dem angegebenen Caddyfile:

`caddy run --config {{pfad/zu/Caddyfile}}`

- Starte Caddy im Hintergrund:

`caddy start`

- Stoppe einen im Hintergrund laufenden Caddy-Prozess:

`caddy stop`

- Führe einen einfachen Dateiserver auf dem angegebenen Port mit einer durchsuchbaren Oberfläche aus:

`caddy file-server --listen :{{8000}} --browse`

- Führe einen Reverse-Proxy-Server aus:

`caddy reverse-proxy --from :{{80}} --to localhost:{{8000}}`
