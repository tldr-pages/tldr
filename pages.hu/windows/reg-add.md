# reg add

> Új kulcsok és értékeik hozzáadása a rendszerleíró adatbázishoz. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-add>.

- Új beállításkulcs hozzáadása:

`reg add {{key_name}}`

- Új érték hozzáadása egy adott kulcs alatt:

`reg add {{key_name}} /v {{value}}`

- Új érték hozzáadása meghatározott adatokkal:

`reg add {{key_name}} /d {{data}}`

- Új érték hozzáadása egy adott adattípusú kulcshoz:

`reg add {{key_name}} /t {{type}}`

- Meglévő beállításjegyzékérték kényszerített felülírása felszólítás nélkül:

`reg add {{key_name}} /f`
