# odps inst

> Példányok kezelése az ODPS-ben (Open Data Processing Service). Lásd még: `odps`. További információ: <https://www.alibabacloud.com/help/doc-detail/27971.htm>.

- Az aktuális felhasználó által létrehozott példányok megjelenítése:

`show instances;`

- Egy példány részleteinek leírása:

`desc instance {{instance_id}};`

- Egy példány állapotának ellenőrzése:

`status {{instance_id}};`

- Várni egy példány befejezésére, addig napló- és folyamatinformációkat nyomtatva:

`wait {{instance_id}};`

- Egy példány megállítása:

`kill {{instance_id}};`
