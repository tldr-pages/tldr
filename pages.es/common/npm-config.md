# npm-config

> Gestiona los ajustes de configuración de `npm`.
> Más información: <https://docs.npmjs.com/cli/commands/npm-config>.

- Muestra todos los ajustes de configuración:

`npm config list`

- Lista todos los ajustes de configuración como `JSON`:

`npm config list --json`

- Obtiene el valor de una clave de configuración específica:

`npm config get {{clave}}`

- Establece una clave de configuración a un valor específico:

`npm config set {{clave}} {{valor}}`

- Elimina una clave de configuración:

`npm config delete {{clave}}`

- Edita el archivo de configuración global de npm en el editor predeterminado:

`npm config edit`

- Intenta reparar elementos de configuración no válidos:

`npm config fix`
