# reg save

> Egy beállításkulcs, annak alkulcsai és értékei mentése egy fájlba. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-save>.

- Egy beállításkulcs, annak alkulcsai és értékei mentése egy adott fájlba:

`reg save {{key_name}} {{path/to/file}}`

- Meglévő fájl kényszerített felülírása felszólítás nélkül:

`reg save {{key_name}} {{path/to/file}} /y`
