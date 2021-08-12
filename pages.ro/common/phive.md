# phive

> Mediul de instalare și verificare Phar pentru implementarea sigură a aplicațiilor PHP.
> Mai multe informaţii: <https://phar.io>

- Afișează o listă de Phars alias disponibile:

`phive list`

- Instalați un Phar specificat în directorul local:

`phive install {{alias|url}}`

- Instalați un Phar specificat la nivel global:

`phive install {{alias|url}} --global`

- Instalați un Phar specificat într-un director țintă:

`phive install {{alias|url}} --target {{path/to/directory}}`

- Actualizați toate fișierele Phar la cea mai recentă versiune:

`phive update`

- Eliminați un fișier Phar specificat:

`phive remove {{alias|url}}`

- Elimină fișierele Phar neutilizate:

`phive purge`

- Listează toate comenzile disponibile:

`phive help`
