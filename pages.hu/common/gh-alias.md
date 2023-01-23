# gh alias

> A GitHub CLI parancs aliasok kezelése a parancssorból. További információk: <https://cli.github.com/manual/gh_alias>.

- Az alparancsok súgójának megjelenítése:

`gh alias`

- A `gh` összes aliasának felsorolása, amelyek használatára a van beállítva:

`gh alias list`

- A `gh` alparancs alias létrehozása:

`gh alias set {{pv}} '{{pr view}}'`

- Egy shell parancs beállítása `gh` alparancsként:

`gh alias set --shell {{alias_name}} {{command}}`

- Parancsparancs parancsszó alárendeltjének törlése:

`gh alias delete {{alias_name}}`
