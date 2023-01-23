# httping

> A webkiszolgáló késleltetésének és átviteli sebességének mérése. További információ: <https://manned.org/httping>.

- Pingelje a megadott URL-címet:

`httping -g {{url}}`

- A webkiszolgáló pingelése a `host` és a `port` oldalon:

`httping -h {{host}} -p {{port}}`

- Pingelje a `host` webkiszolgálót TLS-kapcsolat használatával:

`httping -l -g https://{{host}}`

- A `host` webkiszolgáló pingelése HTTP alapszintű hitelesítéssel:

`httping -g http://{{host}} -U {{username}} -P {{password}}`
