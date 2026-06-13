# objcopy

> Copia el contenido de un archivo de objetos a otro archivo.
> Más información: <https://manned.org/objcopy>.

- Copia datos a otro archivo:

`objcopy {{ruta/al/archivo_de_origen}} {{ruta/al/archivo_de_destino}}`

- Traduce ficheros de un formato a otro:

`objcopy --input-target={{formato_de_entrada}} --output-target {{formato_de_salida}} {{ruta/al/archivo_de_origen}} {{ruta/al/archivo_de_destino}}`

- Elimina toda la información de símbolos del archivo:

`objcopy --strip-all {{ruta/al/archivo_de_origen}} {{ruta/al/archivo_de_destino}}`

- Elimina la información de depuración del archivo:

`objcopy --strip-debug {{ruta/al/archivo_de_origen}} {{ruta/al/archivo_de_destino}}`

- Copia una sección específica del archivo de origen al archivo de destino:

`objcopy --only-section {{section}} {{ruta/al/archivo_de_origen}} {{ruta/al/archivo_de_destino}}`
