# npm

> Gestor de paquetes JavaScript y Node.js.
> Gestiona proyectos de Node.js y sus módulos de dependencias.
> Más información: <https://www.npmjs.com>.

- Creación interactiva de un archivo `package.json`:

`npm init`

- Descarga todos los paquetes listados como dependencias en `package.json`:

`npm install`

- Descarga una versión específica de un paquete y lo añade a la lista de dependencias en `package.json`:

`npm install {{nombre_paquete}}@{{versión}}`

- Descarga la última versión de un paquete y lo añade a la lista de dependencias de desarrollo en `package.json`:

`npm install {{nombre_paquete}} --save-dev`

- Descarga la última versión de un paquete y lo instala globalmente:

`npm install --global {{nombre_paquete}}`

- Desinstala un paquete y lo remueve de la lista de dependencias en `package.json`:

`npm uninstall {{nombre_paquete}}`

- Lista de dependencias instaladas localmente:

`npm list`

- Lista de paquetes instalados globalmente de nivel superior:

`npm list --global --depth={{0}}`
