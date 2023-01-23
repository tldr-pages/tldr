# odps auth

> Felhasználói hatóságok az ODPS-ben (Open Data Processing Service). Lásd még: `odps`. További információ: <https://www.alibabacloud.com/help/doc-detail/27971.htm>.

- Felhasználó hozzáadása az aktuális projekthez:

`add user {{username}};`

- Hatósági jogosultságok megadása egy felhasználónak:

`grant {{action_list}} on {{object_type}} {{object_name}} to user {{username}};`

- Egy felhasználó jogosultságainak megjelenítése:

`show grants for {{username}};`

- Felhasználói szerepkör létrehozása:

`create role {{role_name}};`

- Hatósági jogosultságok megadása egy szerepkörnek:

`grant {{action_list}} on {{object_type}} {{object_name}} to role {{role_name}};`

- Egy szerepkör jogosultságainak leírása:

`desc role {{role_name}};`

- Szerepkör megadása egy felhasználónak:

`grant {{role_name}} to {{username}};`
