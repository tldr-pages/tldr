# balena

> Interakció a balenaCloud, openBalena és a balena API-val a parancssorból. További információ: <https://www.balena.io/docs/reference/cli/>.

- Jelentkezzen be a balenaCloud fiókba:

`balena login`

- Hozzon létre egy balenaCloud vagy openBalena alkalmazást:

`balena app create {{app_name}}`

- A fiókban lévő összes balenaCloud- vagy openBalena-alkalmazás listázása:

`balena apps`

- A balenaCloud- vagy openBalena-fiókhoz tartozó összes eszköz listázása:

`balena devices`

- BalenaOS-kép flashelése egy helyi meghajtóra:

`balena local flash {{path/to/balenaos.img}} --drive {{drive_location}}`
