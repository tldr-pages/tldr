# gh codespace

> Conecta y gestiona tus codespaces en GitHub.
> Más información: <https://cli.github.com/manual/gh_codespace>.

- Crea un codespace en GitHub de forma interactiva:

`gh codespace create`

- Lista todos los codespaces disponibles:

`gh codespace list`

- Conecta a un codespace vía SSH de forma interactiva:

`gh codespace ssh`

- Transfiere un archivo específico a un codespace interactivamente:

`gh codespace cp {{ruta/al/archivo_fuente}} remote:{{ruta/al/archivo_remoto}}`

- Lista los puertos de un codespace interactivo:

`gh codespace ports`

- Muestra los registros (logs) de un codespace interactivo:

`gh codespace logs`

- Elimina un codespace interactivamente:

`gh codespace delete`

- Muestra ayuda para un subcomando:

`gh codespace {{code|cp|create|delete|edit|...}} --help`
