# npm rebuild

> Recompila los paquetes nativos de Node.js tras cambios en Node o en las dependencias.
> Más información: <https://docs.npmjs.com/cli/npm-rebuild/>.

- Recompila un paquete específico:

`npm {{[rb|rebuild]}} {{paquete}}`

- Recompila todos los paquetes instalados:

`npm {{[rb|rebuild]}}`

- Recompila con salida detallada:

`npm {{[rb|rebuild]}} --verbose`

- Recompila un paquete en un directorio específico:

`npm {{[rb|rebuild]}} --prefix {{ruta/al/directorio}} {{paquete}}`

- Recompila sin utilizar la caché de npm:

`npm {{[rb|rebuild]}} --no-cache`

- Recompila en modo global:

`npm {{[rb|rebuild]}} {{[-g|--global]}}`
