# choco list

> A Chocolatey csomagok listájának megjelenítése. További információ: <https://chocolatey.org/docs/commands-list>.

- Az összes elérhető csomag megjelenítése:

`choco list`

- Az összes helyileg telepített csomag megjelenítése:

`choco list --local-only`

- A helyi programokat tartalmazó lista megjelenítése:

`choco list --include-programs`

- Csak a jóváhagyott csomagok megjelenítése:

`choco list --approved-only`

- Egyéni forrás megadása a csomagok megjelenítéséhez:

`choco list --source {{source_url|alias}}`

- Felhasználónév és jelszó megadása a hitelesítéshez:

`choco list --user {{username}} --password {{password}}`
