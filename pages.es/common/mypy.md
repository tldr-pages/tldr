# mypy

> Verificación de código Python.
> Más información: <https://mypy.readthedocs.io/en/stable/running_mypy.html>.

- Comprueba un archivo específico:

`mypy {{ruta/al/archivo.py}}`

- Comprueba un [m]ódulo específico:

`mypy -m {{nombre_del_módulo}}`

- Comprueba un [p]aquete específico:

`mypy -p {{nombre_del_paquete}}`

- Comprueba una cadena de código:

`mypy -c "{{código}}"`

- Ignora importaciones faltantes:

`mypy --ignore-missing-imports {{ruta/al_archivo_o_directorio}}`

- Muestra mensajes de error detallados:

`mypy --show-traceback {{ruta/al/archivo_o_directorio}}`

- Especifica un archivo de configuración personalizado:

`mypy --config-file {{ruta/al/archivo_de_configuración}}`

- Muestra ayuda:

`mypy -h`
