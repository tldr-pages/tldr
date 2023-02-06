# choco search

> Helyi vagy távoli csomag keresése a Chocolatey segítségével. További információ: <https://chocolatey.org/docs/commands-search>.

- Csomag keresése:

`choco search {{query}}`

- Csomag keresése helyileg:

`choco search {{query}} --local-only`

- Csak a pontos egyezéseket tartalmazza a találatok között:

`choco search {{query}} --exact`

- Minden kérést automatikusan megerősít:

`choco search {{query}} --yes`

- Egyéni forrás megadása a csomagok kereséséhez:

`choco search {{query}} --source {{source_url|alias}}`

- Felhasználónév és jelszó megadása a hitelesítéshez:

`choco search {{query}} --user {{username}} --password {{password}}`
