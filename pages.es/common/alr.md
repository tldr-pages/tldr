# alr

> Gestor de paquetes de Ada.
> Gestiona compiladores, dependencias, herramientas y bibliotecas de Ada.
> Más información: <https://alire.ada.dev/docs/#first-steps>.

- Crea un proyecto de un ejecutable (`--bin`) o de una biblioteca (`--lib`):

`alr init {{--bin|--lib}} {{nombre_de_proyecto}}`

- Añade una dependencia al proyecto:

`alr add {{crate}}`

- Ejecuta el ejecutable generado (no es necesario hacer `build` antes de `run`):

`alr run`

- Compila el proyecto:

`alr build {{--release|--development|--validation}}`
