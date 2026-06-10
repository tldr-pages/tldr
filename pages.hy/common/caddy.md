#կադդի

> Ձեռնարկությունների համար պատրաստ բաց կոդով վեբ սերվեր՝ ավտոմատ HTTPS-ով, գրված Go-ում:.
> Լրացուցիչ տեղեկություններ. <https://caddyserver.com/docs/command-line>:.

- Սկսեք Caddy-ն առաջին պլանում.:

`caddy run`

- Սկսեք Caddy-ն նշված Caddyfile-ով.:

`caddy run --config {{path/to/Caddyfile}}`

- Սկսեք Caddy-ն հետին պլանում.:

`caddy start`

- Դադարեցրեք ֆոնային Caddy գործընթացը.:

`caddy stop`

- Գործարկեք պարզ ֆայլերի սերվեր նշված նավահանգստում զննարկվող ինտերֆեյսով.:

`caddy file-server --listen :{{8000}} --browse`

- Գործարկել հակադարձ պրոքսի սերվեր.:

`caddy reverse-proxy --from :{{80}} --to localhost:{{8000}}`
