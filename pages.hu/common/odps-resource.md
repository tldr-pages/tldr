# odps resource

> Az erőforrások kezelése az ODPS-ben (Open Data Processing Service). Lásd még: `odps`. További információ: <https://www.alibabacloud.com/help/doc-detail/27971.htm>.

- Az erőforrások megjelenítése az aktuális projektben:

`list resources;`

- Fájl erőforrás hozzáadása:

`add file {{filename}} as {{alias}};`

- Archívum erőforrás hozzáadása:

`add archive {{archive.tar.gz}} as {{alias}};`

- .jar erőforrás hozzáadása:

`add jar {{package.jar}};`

- .py erőforrás hozzáadása:

`add py {{script.py}};`

- Erőforrás törlése:

`drop resource {{resource_name}};`
