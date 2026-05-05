# komac

> Crea manifiestos WinGet para el repositorio `winget-pkgs`.
> Más información: <https://github.com/russellbanks/Komac>.

- Crea un nuevo paquete desde cero:

`komac new {{Paquete.Identificador}} {{[-v|--version]}} {{1.2.3}} {{[-u|--urls]}} {{https://example.com/app.exe}}`

- Actualiza un paquete existente con una nueva versión:

`komac update {{Paquete.Identificador}} {{[-v|--version]}} {{1.2.3}} {{[-u|--urls]}} {{https://example.com/app.exe}}`

- Actualiza un paquete con varias URL y lo envía automáticamente:

`komac update {{Paquete.Identificador}} {{[-v|--version]}} {{1.2.3}} {{[-u|--urls]}} {{https://example.com/app.exe https://example.com/app.msi ...}} {{[-s|--submit]}}`

- Elimina una versión de winget-pkgs:

`komac remove {{Paquete.Identificador}} {{[-v|--version]}} {{1.2.3}}`

- Lista todas las versiones de un paquete:

`komac {{[list|list-versions]}} {{Paquete.Identificador}}`

- Sincroniza tu fork de winget-pkgs con el repositorio fuente:

`komac {{[sync|sync-fork]}}`

- Actualiza el token de GitHub almacenado:

`komac token {{[add|update]}} {{[-t|--token]}} {{tu_token_github}}`

- Genera una secuencia de comandos de autocompletado del intérprete de comandos:

`komac {{[complete|autocomplete]}} {{bash|elvish|fish|powershell|zsh}}`
