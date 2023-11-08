# mas

> Interfaz de línea de comandos para la Mac App Store.
> Más información: <https://github.com/mas-cli/mas>.

- Inicia sesión en la Mac App Store por primera vez:

`mas signin "{{usuario@ejemplo.com}}"`

- Muestra todas las aplicaciones instaladas y sus identificadores de producto:

`mas list`

- Busca una aplicación, mostrando el precio junto a los resultados:

`mas search " {{aplicación}}" --price`

- Instala o actualiza una aplicación:

`mas install {{identificador_producto}}`

- Instala todas las actualizaciones pendientes:

`mas upgrade`
