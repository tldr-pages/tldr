# atoum

> Un cadru simplu, modern și intuitiv de testare a unităților pentru PHP.
> Mai multe informaţii: <http://atoum.org>

- Iniţializarea unui fişier de configurare:

`atoum --init`

- Rulați toate testele:

`atoum`

- Rulați teste utilizând fișierul de configurare specificat:

`atoum -c {{path/to/file}}`

- Rulați un anumit fișier de testare:

`atoum -f {{path/to/file}}`

- Rulați un anumit director de teste:

`atoum -d {{path/to/directory}}`

- Rulați toate testele sub un anumit spațiu de nume:

`atoum -ns {{namespace}}`

- Rulați toate testele cu o etichetă specifică:

`atoum -t {{tag}}`

- Încărcați un fișier bootstrap personalizat înainte de a rula teste:

`atoum --bootstrap-file {{path/to/file}}`
