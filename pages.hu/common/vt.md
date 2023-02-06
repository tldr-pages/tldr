# vt

> A VirusTotal parancssori interfésze. A parancshoz egy VirusTotal-fiók API-kulcsa szükséges. További információ: <https://github.com/VirusTotal/vt-cli>.

- Egy adott fájl víruskeresése:

`vt scan file {{path/to/file}}`

- Egy URL-cím vírusellenőrzése:

`vt scan url {{url}}`

- Egy adott elemzésből származó információk megjelenítése:

`vt analysis {{file_id|analysis_id}}`

- Fájlok letöltése titkosított `.zip` formátumban (prémium fiók szükséges):

`vt download {{file_id}} --output {{path/to/directory}} --zip --zip-password {{password}}`

- A `vt` inicializálása vagy újrainicializálása az API-kulcs interaktív megadásához:

`vt init`

- Egy tartományra vonatkozó információk megjelenítése:

`vt domain {{url}}`

- Információk megjelenítése egy adott URL-hez:

`vt url {{url}}`

- Egy adott IP-címre vonatkozó információk megjelenítése:

`vt domain {{ip_address}}`
