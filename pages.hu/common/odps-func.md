# odps func

> Az ODPS (Open Data Processing Service) funkcióinak kezelése. Lásd még: `odps`. További információ: <https://www.alibabacloud.com/help/doc-detail/27971.htm>.

- Az aktuális projektben lévő funkciók megjelenítése:

`list functions;`

- Java-funkció létrehozása a `.jar` erőforrás használatával:

`create function {{func_name}} as {{path.to.package.Func}} using '{{package.jar}}';`

- Python függvény létrehozása a `.py` erőforrás használatával:

`create function {{func_name}} as {{script.Func}} using '{{script.py}}';`

- Egy függvény törlése:

`drop function {{func_name}};`
