# wp

> Interfața oficială a liniei de comandă pentru a gestiona instanțele WordPress.
> Mai multe informaţii: <https://wp-cli.org/>

- Imprimați informații despre instalarea sistemului de operare, shell, PHP și WP-CLI (`wp`):

`wp --info`

- Actualizare WP-CLI:

`wp cli update`

- Instalați și activați un plugin WordPress:

`wp plugin install {{plugin}} --activate`

- Înlocuiți toate instanțele unui șir în baza de date:

`wp search-replace {{old_string}} {{new_string}}`

- Importați conținutul unui fișier WordPress Extended RSS (WXR):

`wp import {{path/to/file.xml}}`
