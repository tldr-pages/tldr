# npm exec

> Ejecuta binarios de paquetes `npm`.
> Más información: <https://docs.npmjs.com/cli/npm-exec/>.

- Ejecuta el comando desde un paquete `npm` local o remoto:

`npm {{[x|exec]}} {{comando}} {{argumento1 argumento2 ...}}`

- Especifica el paquete explícitamente (útil si existen varios comandos con el mismo nombre):

`npm {{[x|exec]}} --package {{paquete}} {{comando}}`

- Ejecuta un comando si existe en la ruta actual o en `node_modules/.bin`:

`npm {{[x|exec]}} --no-install {{comando}} {{argumento1 argumento2 ...}}`

- Ejecuta un comando específico, suprimiendo cualquier salida del propio `npm`:

`npm {{[x|exec]}} --quiet {{comando}} {{argumento1 argumento2 ...}}`

- Muestra la ayuda:

`npm {{[x|exec]}} --help`
