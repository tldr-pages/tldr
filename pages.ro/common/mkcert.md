# mkcert

> Instrument pentru realizarea certificatelor de dezvoltare de încredere la nivel local.
> Mai multe informaţii: <https://github.com/FiloSottile/mkcert>

- Instalați CA local în magazinul de încredere sistem:

`mkcert -install`

- Generarea certificatului și a cheii private pentru un domeniu dat:

`mkcert {{example.org}}`

- Generarea certificatului și a cheii private pentru mai multe domenii:

`mkcert {{example.org}} {{myapp.dev}} {{127.0.0.1}}`

- Generați certificat wildcard și cheie privată pentru un domeniu dat și subdomeniile sale:

`mkcert "{{*.example.it}}"`

- Dezinstalați CA locale:

`mkcert -uninstall`
