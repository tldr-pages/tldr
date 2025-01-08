# objdump

> Muestra información sobre los archivos objeto.
> Más información: <https://manned.org/objdump>.

- Muestra la información del encabezado del archivo:

`objdump -f {{ruta/al/binario}}`

- Muestra toda la información del encabezado:

`objdump -x {{ruta/al/binario}}`

- Muestra la salida desensamblada (disassembled) de secciones ejecutables:

`objdump -d {{ruta/al/binario}}`

- Muestra las secciones ejecutables desensambladas con sintaxis Intel:

`objdump -M intel -d {{ruta/al/binario}}`

- Muestra un volcado hexadecimal ruta/al/binario completo de todas las secciones:

`objdump -s {{ruta/al/binario}}`
