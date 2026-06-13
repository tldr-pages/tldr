# objdump

> Muestra información sobre los archivos objeto.
> Más información: <https://manned.org/objdump>.

- Muestra la información del encabezado del archivo:

`objdump {{[-f|--file-headers]}} {{ruta/al/binario}}`

- Muestra toda la información del encabezado:

`objdump {{[-x|--all-headers]}} {{ruta/al/binario}}`

- Muestra la salida desensamblada (disassembled) de secciones ejecutables:

`objdump {{[-d|--disassemble]}} {{ruta/al/binario}}`

- Muestra las secciones ejecutables desensambladas con sintaxis Intel:

`objdump {{[-M|--disassembler-options]}} intel {{[-d|--disassemble]}} {{ruta/al/binario}}`

- Muestra un volcado hexadecimal ruta/al/binario completo de todas las secciones:

`objdump {{[-s|--full-contents]}} {{ruta/al/binario}}`
