# you-get

> Médiatartalmak (videók, hanganyagok, képek) letöltése a világhálóról. További információ: <https://you-get.org>.

- Médiainformációk nyomtatása egy adott médiáról a weben:

`you-get --info {{https://example.com/video?id=value}}`

- Médiatartalom letöltése egy adott URL-címről:

`you-get {{https://example.com/video?id=value}}`

- Keresés a Google Videókon és letöltés:

`you-get {{keywords}}`

- Egy médiatartalom letöltése egy adott helyre:

`you-get --output-dir {{path/to/directory}} --output-filename {{filename}} {{https://example.com/watch?v=value}}`

- Média letöltése proxy használatával:

`you-get --http-proxy {{proxy_server}} {{https://example.com/watch?v=value}}`
