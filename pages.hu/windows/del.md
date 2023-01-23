# del

> Egy vagy több fájl törlése. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/del>.

- Egy vagy több, szóközzel elválasztott fájl vagy minta törlése:

`del {{file_pattern}}`

- Minden egyes fájl törlése előtt megerősítést kér:

`del {{file_pattern}} /p`

- Csak olvasható fájlok törlésének kikényszerítése:

`del {{file_pattern}} /f`

- Fájl(ok) rekurzív törlése minden alkönyvtárból:

`del {{file_pattern}} /s`

- Ne kérdezzen, ha fájlokat töröl egy globális helyettesítő jelszó alapján:

`del {{file_pattern}} /q`

- A súgó megjelenítése és az elérhető attribútumok listája:

`del /?`

- Fájlok törlése megadott attribútumok alapján:

`del {{file_pattern}} /a {{attribute}}`
