# caddy

> Un server web cu sursă deschisă, puternic, pregătit pentru întreprindere, cu HTTPS automat, scris în Go.
> Mai multe informaţii: <https://caddyserver.com>

- Porniți Caddy în prim-plan:

`caddy run`

- Porniți Caddy cu Caddyfile specificat:

`caddy run --config {{path/to/Caddyfile}}`

- Porniți Caddy în fundal:

`caddy start`

- Opriți un proces de fundal Caddy:

`caddy stop`

- Rulați un server de fișiere simplu pe portul specificat cu o interfață browsabilă:

`caddy file-server --listen :{{8000}} --browse`

- Rulați un server proxy invers:

`caddy reverse-proxy --from :{{80}} --to localhost:{{8000}}`
