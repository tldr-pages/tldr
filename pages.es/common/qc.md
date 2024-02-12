# qc

> Gestiona y ejecuta fragmentos de comandos almacenados en notas QOwnNotes.
> Ve también: `qownnotes`.
> Más información: <https://www.qownnotes.org/getting-started/command-line-snippet-manager.html>.

- Configura el gestor de fragmentos, por ejemplo para establecer el token de seguridad de QOwnNotes:

`qc configure`

- Busca e imprime fragmentos de comandos almacenados en tu nota `Commands.md` y en todas tus notas etiquetadas con `commands`:

`qc search`

- Ejecuta un fragmento y muestra el comando antes de ejecutarlo:

`qc exec --command`

- Ejecuta el último fragmento y muestra el comando antes de ejecutarlo:

`qc exec --command --last`

- Cambia entre las carpetas de notas en QOwnNotes:

`qc switch`
