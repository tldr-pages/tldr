# objdump

> Bekijk informatie over object bestanden.
> Meer informatie: <https://manned.org/objdump>.

- Toon de bestand header informatie:

`objdump {{[-f|--file-headers]}} {{pad/naar/binary}}`

- Toon alle header informatie:

`objdump {{[-x|--all-headers]}} {{pad/naar/binary}}`

- Toon de gedemonteerde uitvoer van uitvoerbare secties:

`objdump {{[-d|--disassemble]}} {{pad/naar/binary}}`

- Toon de gedemonteerde uitvoer van uitvoerbare secties in intel syntax:

`objdump {{[-M|--disassembler-options]}} intel {{[-d|--disassemble]}} {{pad/naar/binary}}`

- Toon de symbooltabel:

`objdump {{[-t|--syms]}} {{pad/naar/binary}}`

- Toon een complete binary hex dump van alle secties:

`objdump {{[-s|--full-contents]}} {{pad/naar/binary}}`
