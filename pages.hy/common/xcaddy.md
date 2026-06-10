# xcaddy

> Caddy Web Server-ի անհատական կառուցման գործիք:.
> Լրացուցիչ տեղեկություններ. <https://github.com/caddyserver/xcaddy#command-usage>:.

- Կառուցեք Caddy սերվեր աղբյուրից.:

`xcaddy build`

- Կառուցեք Caddy սերվերը հատուկ տարբերակով (կանխադրված մինչև վերջինը).:

`xcaddy build {{version}}`

- Կառուցեք Caddy հատուկ մոդուլով.:

`xcaddy build --with {{module_name}}`

- Կառուցեք Caddy և թողարկեք որոշակի ֆայլ.:

`xcaddy build --output {{path/to/file}}`

- Կառուցեք և գործարկեք Caddy-ն ընթացիկ գրացուցակում զարգացման հավելվածի համար.:

`xcaddy run`

- Կառուցեք և գործարկեք Caddy-ն զարգացման հավելվածի համար՝ օգտագործելով Caddy-ի հատուկ կոնֆիգուրացիա.:

`xcaddy run --config {{path/to/file}}`
