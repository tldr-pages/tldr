# choco outdated

> Ellenőrizze a Chocolatey-nál, hogy a csomagok elavultak-e. További információ: <https://chocolatey.org/docs/commands-outdated>.

- Az elavult csomagok listájának megjelenítése táblázatos formában:

`choco outdated`

- A kimeneten figyelmen kívül hagyja a kitűzött csomagokat:

`choco outdated --ignore-pinned`

- Egyéni forrás megadása a csomagok ellenőrzéséhez:

`choco outdated --source {{source_url|alias}}`

- Adjon meg egy felhasználónevet és jelszót a hitelesítéshez:

`choco outdated --user {{username}} --password {{password}}`
