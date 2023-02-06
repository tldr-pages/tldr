# choco upgrade

> Egy vagy több csomag frissítése Chocolatey-val. További információ: <https://chocolatey.org/docs/commands-upgrade>.

- Egy vagy több, szóközzel elválasztott csomag frissítése:

`choco upgrade {{package(s)}}`

- Frissítés egy csomag egy adott verziójára:

`choco upgrade {{package}} --version {{version}}`

- Az összes csomag frissítése:

`choco upgrade all`

- Minden csomag frissítése, kivéve a megadott, vesszővel elválasztott csomagokat:

`choco upgrade all --except "{{package(s)}}"`

- Minden kérés automatikus megerősítése:

`choco upgrade {{package}} --yes`

- Egyéni forrás megadása a csomagok fogadásához:

`choco upgrade {{package}} --source {{source_url|alias}}`

- Felhasználónév és jelszó megadása a hitelesítéshez:

`choco upgrade {{package}} --user {{username}} --password {{password}}`
