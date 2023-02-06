# doctl auth

> A doctl hitelesítés egy vagy több API-tokennel. További információ: <https://docs.digitalocean.com/reference/doctl/reference/auth/>.

- Nyisson meg egy promptot egy API-token megadásához és címkézze fel a kontextusát:

`doctl auth init --context {{token_label}}`

- Hitelesítési kontextusok (API-tokenek) listázása:

`doctl auth list`

- Kontextusok (API-tokenek) váltása:

`doctl auth switch --context {{token_label}}`

- Tárolt hitelesítési kontextus (API-token) eltávolítása:

`doctl auth remove --context {{token_label}}`

- Elérhető parancsok megjelenítése:

`doctl auth --help`
