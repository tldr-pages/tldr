# olevba

> Analiza archivos OLE y OpenXML (p. ej., DOC, XLS, PPT, etc.) para extraer macros VBA, desofuscar y analizar código malicioso.
> Parte de la suite `python-oletools`.
> Más información: <https://github.com/decalage2/oletools>.

- Analiza un archivo, mostrando tanto el código de la macro como los resultados del análisis:

`olevba {{ruta/al/archivo}}`

- Analiza recursivamente todos los archivos compatibles de un directorio:

`olevba -r {{ruta/al/directorio}}`

- Proporciona una contraseña para los archivos cifrados de Microsoft Office (puede repetirse):

`olevba --password {{contraseña}} {{ruta/al/archivo_encriptado}}`

- Muestra solo los resultados del análisis, sin mostrar el código fuente de la macro:

`olevba -a {{ruta/al/archivo}}`

- Muestra solo el código fuente de la macro:

`olevba -c {{ruta/al/archivo}}`

- Muestra cadenas ofuscadas y su contenido decodificado:

`olevba --decode {{ruta/al/archivo}}`
