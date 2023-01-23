# reg compare

> A kulcsok és értékeik összehasonlítása a rendszerleíró adatbázisban. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-compare>.

- Egy adott kulcs alatti összes érték összehasonlítása egy második kulccsal:

`reg compare {{first_key_name}} {{second_key_name}}`

- Egy adott érték összehasonlítása két kulcs alatt:

`reg compare {{first_key_name}} {{second_key_name}} /v {{value}}`

- Két kulcs összes alkulcsának és értékének összehasonlítása:

`reg compare {{first_key_name}} {{second_key_name}} /s`

- Csak a megadott kulcsok közötti egyezéseket adja ki:

`reg compare {{first_key_name}} {{second_key_name}} /os`

- A megadott kulcsok közötti különbségek és egyezések kiadása:

`reg compare {{first_key_name}} {{second_key_name}} /oa`
