# atoum

> Un framework de pruebas unitarias para PHP sencillo, moderno e intuitivo.
> Más información: <http://atoum.org>.

- Inicializa un fichero de configuración:

`atoum --init`

- Ejecuta todas las pruebas:

`atoum`

- Ejecuta pruebas utilizando el archivo de configuración especificado:

`atoum -c {{ruta/al/archivo}}`

- Ejecuta un archivo de prueba específico:

`atoum -f {{ruta/al/archivo}}`

- Ejecuta un directorio específico de pruebas:

`atoum -d {{ruta/al/directorio}}`

- Ejecuta todas las pruebas dado un namespace específico:

`atoum -ns {{namespace}}`

- Ejecuta todas las pruebas dada una etiqueta específica:

`atoum -t {{etiqueta}}`

- Carga un archivo bootstrap personalizado antes de ejecutar las pruebas:

`atoum --bootstrap-file {{ruta/al/archivo}}`
