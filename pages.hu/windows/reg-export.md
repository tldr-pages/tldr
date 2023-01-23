# reg export

> A megadott alkulcsok és értékek exportálása egy fájlba. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-export>.

- Egy adott kulcs összes alkulcsának és értékének exportálása:

`reg export {{key_name}} {{path/to/file.reg}}`

- Meglévő fájl felülírásának kikényszerítése felszólítás nélkül:

`reg export {{key_name}} {{path/to/file.reg}} /y`
