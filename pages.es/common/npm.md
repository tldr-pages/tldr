# npm

> Gestor de paquetes JavaScript y Node.js.
> Gestiona proyectos Node.js y sus dependencias de módulos.
> Más información: <https://docs.npmjs.com/cli/npm>.

- Crea un archivo `package.json` con los valores por defecto (omite --yes para hacerlo de forma interactiva):

`npm init {{[-y|--yes]}}`

- Descarga todos los paquetes alistados como dependencias en `package.json`:

`npm {{[i|install]}}`

- Descarga una versión específica de un paquete y lo añade a la lista de dependencias en `package.json`:

`npm {{[i|install]}} {{nombre_paquete}}@{{versión}}`

- Descarga la última versión de un paquete y lo añade a la lista de dependencias de desarrollo en `package.json`:

`npm {{[i|install]}} {{nombre_paquete}} {{[-D|--save-dev]}}`

- Descarga la última versión de un paquete y lo instala globalmente:

`npm {{[i|install]}} {{[-g|--global]}} {{nombre_paquete}}`

- Desinstala un paquete y lo elimina de la lista de dependencias en `package.json`:

`npm {{[r|uninstall]}} {{nombre_paquete}}`

- Lista de dependencias instaladas localmente:

`npm {{[ls|list]}}`

- Lista los paquetes instalados globalmente:

`npm {{[ls|list]}} {{[-g|--global]}} --depth {{0}}`
