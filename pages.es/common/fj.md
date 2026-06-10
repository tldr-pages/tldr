# fj

> Interactúa con instancias de Forgejo desde la terminal.
> Más información: <https://codeberg.org/forgejo-contrib/forgejo-cli>.

- Inicia sesión en una instancia de Forgejo:

`fj auth login`

- Clona un repositorio de Forgejo localmente:

`fj repo clone {{propietario}}/{{repositorio}}`

- Crea un nuevo issue en el repositorio actual:

`fj issue create`

- Abre un issue en el navegador web por defecto:

`fj issue browse {{numero_de_issue}}`

- Crea un nuevo pull request:

`fj pr create`

- Descarga un pull request específico en una nueva rama local:

`fj pr checkout {{numero_de_pr}}`

- Lista todas las releases del repositorio actual:

`fj release list`

- Muestra el usuario autenticado actualmente:

`fj whoami`
