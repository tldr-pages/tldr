# mas

> Interfaz de línea de comandos para la Mac App Store.
> Más información: <https://github.com/mas-cli/mas>.

- Inicia sesión en la Mac App Store por primera vez:

`mas signin "{{usuario@example.com}}"`

- Muestra todas las aplicaciones instaladas y sus identificadores de producto:

`mas list`

- Busca una aplicación, mostrando el precio junto a los resultados:

`mas search "{{aplicación}}" --price`

- Instala o actualiza una aplicación utilizando el identificador numérico exacto:

`mas install {{id_producto_numérico}}`

- Instala la primera aplicación que devuelva la búsqueda correspondiente:

`mas lucky "{{término_de_búsqueda}}"`

- Lista todas las aplicaciones obsoletas con actualizaciones pendientes:

`mas outdated`

- Instala todas las actualizaciones pendientes:

`mas upgrade`

- Actualiza una aplicación específica:

`mas upgrade "{{id_producto_numérico}}"`
