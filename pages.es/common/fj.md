# fj

> Interactúa con instancias de Forgejo desde la terminal.
> Más información: <https://codeberg.org/forgejo-contrib/forgejo-cli>.

- Inicia sesión en una instancia de Forgejo:

`fj auth login`

- Clona un repositorio de Forgejo de manera local:

`fj repo clone {{propietario}}/{{repositorio}}`

- Crea una nueva incidencia en el repositorio actual:

`fj issue create`

- Abre una incidencia en el navegador web por defecto:

`fj issue browse {{numero_de_la_incidencia}}`

- Crea una nueva solicitud de extracción:

`fj pr create`

- Descarga una solicitud de extracción específico en una nueva rama local:

`fj pr checkout {{numero_de_pr}}`

- Lista todos los lanzamientos del repositorio actual:

`fj release list`

- Muestra el usuario autenticado actualmente:

`fj whoami`
