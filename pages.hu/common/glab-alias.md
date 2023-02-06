# glab alias

> A GitLab CLI parancs aliasok kezelése a parancssorból. További információk: <https://glab.readthedocs.io/en/latest/alias>.

- Az alparancsok súgójának megjelenítése:

`glab alias`

- A `glab` összes aliasának felsorolása, amelyek használatára a be van állítva:

`glab alias list`

- A `glab` alparancs alias létrehozása:

`glab alias set {{mrv}} '{{mr view}}'`

- Egy shell parancs beállítása a `glab` alparancsaként:

`glab alias set --shell {{alias_name}} {{command}}`

- Parancsparancs parancsszó alárendeltjének törlése:

`glab alias delete {{alias_name}}`
