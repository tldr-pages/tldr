# odps resource

> Gestionați resursele în ODPS (Serviciul de procesare a datelor deschise).
> A se vedea, de asemenea, `odps`.
> Mai multe informaţii: <https://www.alibabacloud.com/help/doc-detail/27971.htm>

- Afișați resursele în proiectul curent:

`list resources;`

- Adaugă resurse de fișier:

`add file {{filename}} as {{alias}};`

- Adăugați resurse de arhivă:

`add archive {{archive.tar.gz}} as {{alias}};`

- Adaugă resursă.jar:

`add jar {{package.jar}};`

- Adaugă resursă.py:

`add py {{script.py}};`

- Ștergeți resursa:

`drop resource {{resource_name}};`
