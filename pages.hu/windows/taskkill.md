# taskkill

> Egy folyamat megszüntetése a folyamat azonosítója vagy neve alapján. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/taskkill>.

- Egy folyamat megszüntetése a folyamat azonosítója alapján:

`taskkill /pid {{process_id}}`

- Folyamat megszüntetése a neve alapján:

`taskkill /im {{process_name}}`

- Egy megadott folyamat kényszerített befejezése:

`taskkill /pid {{process_id}} /f`

- Folyamat és gyermekfolyamatai megszüntetése:

`taskkill /im {{process_name}} /t`

- Egy távoli gépen lévő folyamat megszüntetése:

`taskkill /pid {{process_id}} /s {{remote_name}}`

- A parancs használatára vonatkozó információk megjelenítése:

`taskkill /?`
