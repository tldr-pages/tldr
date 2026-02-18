# black

> Formatea código Python automáticamente.
> Vea también: `ruff`.
> Más información: <https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html>.

- Autoformatea un archivo o directorio entero:

`black {{ruta/al/archivo_o_directorio}}`

- Formatea el código pasado como cadena:

`black {{[-c|--code]}} "{{código}}"`

- Muestra si un archivo o un directorio sufrirían cambios en caso de ser formateados:

`black --check {{ruta/al_archivo_o_directorio}}`

- Muestra los cambios que se realizarían en un archivo o directorio sin ejecutarlos (ejecución en seco):

`black --diff {{ruta/a/archivo_o_directorio}}`

- Autoformatea un fichero o directorio, emitiendo exclusivamente mensajes de error a `stderr`:

`black {{[-q|--quiet]}} {{ruta/al/archivo_o_directorio}}`

- Autoformatea un archivo o directorio sin reemplazar las comillas simples por comillas dobles (ayuda para la adopción, evite usar esto para proyectos nuevos):

`black {{[-S|--skip-string-normalization]}} {{ruta/al/archivo_o_directorio}}`
