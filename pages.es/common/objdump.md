# objdump

> Muestra información sobre los archivos objeto.
> Más información: <https://manned.org/objdump>.

- Muestra la información del encabezado del archivo:

`objdump -f {{binario}}`

- Muestra toda la información del encabezado:

`objdump -x {{binario}}`

- Muestra la salida desensamblada (disassembled) de secciones ejecutables:

`objdump -d {{binario}}`

- Muestra las secciones ejecutables desensambladas con sintaxis intel:

`objdump -M intel -d {{binario}}`

- Muestra un volcado hexadecimal binario completo de todas las secciones:

`objdump -s {{binary}}`
