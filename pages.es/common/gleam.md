# gleam

> El compilador, la herramienta de compilación, el gestor de paquetes y el formateador de código para Gleam, "un lenguaje amigable para construir sistemas de tipo seguro escalables".
> Más información: <https://gleam.run/writing-gleam/command-line-reference/>.

- Crea un nuevo proyecto gleam:

`gleam new {{nombre_del_proyecto}}`

- Construye y ejecuta un proyecto gleam:

`gleam run`

- Construye el proyecto:

`gleam build`

- Ejecuta un proyecto para una plataforma y un tiempo de ejecución específico:

`gleam run --target {{plataforma}} --runtime {{tiempo_de_ejecución}}`

- Añade una dependencia hexadecimal a tu proyecto:

`gleam add {{nombre_de_la_dependencia}}`

- Ejecuta las pruebas del proyecto:

`gleam test`

- Formatea el código fuente:

`gleam format`

- Comprueba el tipo de proyecto:

`gleam check`
