# atoum

> Un framework de pruebas unitarias para PHP sencillo, moderno e intuitivo.
> Más información: <https://atoum.readthedocs.io/en/latest/option_cli.html>.

- Inicializa un fichero de configuración:

`atoum --init`

- Ejecuta todas las pruebas:

`atoum`

- Ejecuta pruebas utilizando el archivo de configuración especificado:

`atoum {{[-c|--configuration]}} {{ruta/al/archivo}}`

- Ejecuta un archivo de prueba específico:

`atoum {{[-f|--files]}} {{ruta/al/archivo}}`

- Ejecuta un directorio específico de pruebas:

`atoum {{[-d|--directories]}} {{ruta/al/directorio}}`

- Ejecuta todas las pruebas dado un namespace específico:

`atoum {{[-ns|--namespaces]}} {{namespace}}`

- Ejecuta todas las pruebas dada una etiqueta específica:

`atoum {{[-t|--tags]}} {{etiqueta}}`

- Carga un archivo bootstrap personalizado antes de ejecutar las pruebas:

`atoum {{[-bf|--bootstrap-file]}} {{ruta/al/archivo}}`
