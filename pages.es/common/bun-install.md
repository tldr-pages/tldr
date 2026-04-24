# bun install

> Instala las dependencias de JavaScript de un proyecto a partir de `package.json`.
> Más información: <https://bun.com/docs/pm/cli/install>.

- Instala todas las dependencias que figuran en `package.json`:

`bun {{[i|install]}}`

- Instala un solo paquete (esto es un alias de `bun add`):

`bun {{[i|install]}} {{nombre_paquete}}@{{versión}}`

- Instala un paquete globalmente:

`bun {{[i|install]}} {{[-g|--global]}} {{nombre_paquete}}`

- Instala solo las dependencias de producción (omite `devDependencies`):

`bun {{[i|install]}} {{[-p|--production]}}`

- Instala las dependencias exactamente según el archivo de bloqueo `bun.lockb` (archivo de bloqueo congelado):

`bun {{[i|install]}} --frozen-lockfile`

- Fuerza la descarga de todos los paquetes desde el registro, ignorando la caché:

`bun {{[i|install]}} {{[-f|--force]}}`
