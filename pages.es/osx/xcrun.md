# xcrun

> Ejecuta o localiza herramientas de desarrollo y propiedades.
> Más información: <https://www.unix.com/man-page/osx/1/xcrun/>.

- Localiza y ejecuta una herramienta desde el directorio activo de desarrolladores:

`xcrun {{herramienta}} {{argumentos}}`

- Muestra resultados detallados:

`xcrun {{herramienta}} {{argumentos}} --verbose`

- Busca una herramienta para un SDK determinado:

`xcrun --sdk {{nombre_sdk}}`

- Busca una herramienta para una cadena de herramientas determinada:

`xcrun --toolchain {{nombre}}`

- Muestra versión:

`xcrun --version`

- Muestra ayuda:

`xcrun --help`
