# pydocstyle

> Comprueba estáticamente que los scripts de Python cumplen con las convenciones de documentación de Python.
> Más información: <https://www.pydocstyle.org/en/latest/>.

- Analiza un script de Python o todos los scripts de Python en un directorio específico:

`pydocstyle {{archivo.py|ruta/al/directorio}}`

- Muestra una explicación de cada error:

`pydocstyle {{-e|--explain}} {{archivo.py|ruta/al/directorio}}`

- Muestra información de depuración:

`pydocstyle {{-d|--debug}} {{archivo.py|ruta/al/directorio}}`

- Muestra el número total de errores:

`pydocstyle --count {{archivo.py|ruta/a/directorio}}`

- Utiliza un archivo de configuración específico:

`pydocstyle --config {{ruta/a/archivo_config}} {{archivo.py|ruta/al/directorio}}`

- Ignora uno o más errores:

`pydocstyle --ignore {{D101,D2,D107,...}} {{archivo.py|ruta/al/directorio}}`

- Busca errores de una convención específica:

`pydocstyle --convention {{pep257|numpy|google}} {{archivo.py|ruta/a/directorio}}`
