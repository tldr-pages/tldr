# reg copy

> Kulcsok és értékeik másolása a rendszerleíró adatbázisban. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-copy>.

- Egy beállításkulcs másolása egy új beállítási helyre:

`reg copy {{old_key_name}} {{new_key_name}}`

- Egy beállításkulcs rekurzív módon történő másolása egy új beállítási helyre:

`reg copy {{old_key_name}} {{new_key_name}} /s`

- Regisztrációs kulcs kényszerített másolása kérés nélkül:

`reg copy {{old_key_name}} {{new_key_name}} /f`
