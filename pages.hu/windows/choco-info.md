# choco info

> Részletes információk megjelenítése egy csomagról Chocolatey segítségével. További információ: <https://chocolatey.org/docs/commands-info>.

- Egy adott csomagra vonatkozó információk megjelenítése:

`choco info {{package}}`

- Csak egy helyi csomagra vonatkozó információk megjelenítése:

`choco info {{package}} --local-only`

- Egyéni forrás megadása, ahonnan a csomagok adatait kapja:

`choco info {{package}} --source {{source_url|alias}}`

- Felhasználónév és jelszó megadása a hitelesítéshez:

`choco info {{package}} --user {{username}} --password {{password}}`
