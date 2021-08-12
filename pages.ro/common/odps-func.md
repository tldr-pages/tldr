# odps func

> Gestionați funcțiile în ODPS (Open Data Processing Service).
> A se vedea, de asemenea, `odps`.
> Mai multe informaţii: <https://www.alibabacloud.com/help/doc-detail/27971.htm>

- Afișați funcțiile în proiectul curent:

`list functions;`

- Creați o funcție Java utilizând o resursă `.jar`:

`create function {{func_name}} as {{path.to.package.Func}} using '{{package.jar}}';`

- Creați o funcție Python utilizând o resursă `.py`:

`create function {{func_name}} as {{script.Func}} using '{{script.py}}';`

- Şterge o funcţie:

`drop function {{func_name}};`
