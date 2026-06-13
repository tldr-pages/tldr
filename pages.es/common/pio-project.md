# pio project

> Administra proyectos PlatformIO.
> Más información: <https://docs.platformio.org/en/latest/core/userguide/project/>.

- Inicializa un nuevo proyecto PlatformIO:

`pio project init`

- Inicializa un nuevo proyecto PlatformIO en un directorio específico:

`pio project init {{[-d|--project-dir]}} {{ruta/al/directorio_del_proyecto}}`

- Inicializa un nuevo proyecto PlatformIO, especificando un ID del board:

`pio project init {{[-b|--board]}} {{ATmega328P|uno|...}}`

- Inicializa un nuevo proyecto PlatformIO, especificando una o más opciones para el proyecto:

`pio project init {{[-O|--project-option]}} "{{opción}}={{valor}}" {{[-O|--project-option]}} "{{opción}}={{valor}}"`

- Muestra la configuración de un proyecto:

`pio project config`
