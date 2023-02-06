# pio team

> PlatformIO csapatok kezelése. További információ: <https://docs.platformio.org/en/latest/core/userguide/team/>.

- Hozzon létre egy új csapatot a megadott leírással:

`pio team create --description {{description}} {{organization_name}}:{{team_name}}`

- Csapat törlése:

`pio team destroy {{organization_name}}:{{team_name}}`

- Új felhasználó hozzáadása egy csapathoz:

`pio team add {{organization_name}}:{{team_name}} {{username}}`

- Felhasználó eltávolítása egy csapatból:

`pio team remove {{organization_name}}:{{team_name}} {{username}}`

- Az összes csapat listázása, amelynek a felhasználó tagja, és azok tagjai:

`pio team list`

- A szervezet összes csapatának listázása:

`pio team list {{organization_name}}`

- Egy csapat átnevezése:

`pio team update --name {{new_team_name}} {{organization_name}}:{{team_name}}`

- Egy csapat leírásának módosítása:

`pio team update --description {{new_description}} {{organization_name}}:{{team_name}}`
