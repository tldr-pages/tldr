# reg query

> A beállításjegyzékben lévő kulcsok és alkulcsok értékeinek megjelenítése. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-query>.

- Egy kulcs összes értékének megjelenítése:

`reg query {{key_name}}`

- Egy kulcs egy adott értékének megjelenítése:

`reg query {{key_name}} /v {{value}}`

- Egy kulcs és az alkulcsok összes értékének megjelenítése:

`reg query {{key_name}} /s`

- Egy adott mintának megfelelő kulcsok és értékek keresése:

`reg query {{key_name}} /f "{{query_pattern}}"`

- Megadott adattípusnak megfelelő kulcs értékének megjelenítése:

`reg query {{key_name}} /t {{type}}`
