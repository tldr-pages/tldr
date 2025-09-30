# npm config

> Gestiona los ajustes de configuración de `npm`.
> Más información: <https://docs.npmjs.com/cli/npm-config>.

- Muestra todos los ajustes de configuración:

`npm {{[c|config]}} list`

- Lista todos los ajustes de configuración como `JSON`:

`npm {{[c|config]}} list --json`

- Obtiene el valor de una clave de configuración específica:

`npm {{[c|config]}} get {{clave}}`

- Establece una clave de configuración a un valor específico:

`npm {{[c|config]}} set {{clave}} {{valor}}`

- Elimina una clave de configuración:

`npm {{[c|config]}} delete {{clave}}`

- Edita el archivo de configuración global npm en el editor por defecto:

`npm {{[c|config]}} edit`

- Intentar reparar elementos de configuración no válidos:

`npm {{[c|config]}} fix`
