# xcaddy

> Instrumentul de compilare particularizată pentru serverul Caddy Web.
> Mai multe informaţii: <https://github.com/caddyserver/xcaddy>

- Construiți serverul Caddy de la sursă:

`xcaddy build`

- Construi server Caddy cu o versiune specifică (implicite la cele mai recente):

`xcaddy build {{version}}`

- Construi Caddy cu un modul specific:

`xcaddy build --with {{module_name}}`

- Construiți Caddy și ieșiți într-un anumit fișier:

`xcaddy build --output {{path/to/file}}`

- Construiți și rulați Caddy pentru un plugin de dezvoltare în directorul curent:

`xcaddy run`

- Construiți și rulați Caddy pentru un plugin de dezvoltare folosind un anumit Caddy config:

`xcaddy run --config {{path/to/file}}`
