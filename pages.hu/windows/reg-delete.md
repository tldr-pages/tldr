# reg delete

> Kulcsok vagy értékeik törlése a rendszerleíró adatbázisból. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-delete>.

- Egy adott beállításkulcs törlése:

`reg delete {{key_name}}`

- Egy adott kulcs alatti érték törlése:

`reg delete {{key_name}} /v {{value}}`

- A megadott kulcs alatti összes érték rekurzív törlése:

`reg delete {{key_name}} /va`

- Kényszerített törlés minden érték rekurzívan egy kulcs alatt, felszólítás nélkül:

`reg delete {{key_name}} /f /va`
