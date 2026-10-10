# objdump

> Bekijk informatie over objectbestanden.
> Meer informatie: <https://manned.org/objdump>.

- Toon de bestandsheaderinformatie:

`objdump {{[-f|--file-headers]}} {{pad/naar/binary}}`

- Toon alle headerinformatie:

`objdump {{[-x|--all-headers]}} {{pad/naar/binary}}`

- Toon de gedemonteerde uitvoer van uitvoerbare secties:

`objdump {{[-d|--disassemble]}} {{pad/naar/binary}}`

- Toon de gedemonteerde uitvoer van uitvoerbare secties in Intel-syntax:

`objdump {{[-d|--disassemble]}} {{pad/naar/binary}} {{[-M|--disassembler-options]}} intel`

- Toon de gedemonteerde uitvoer van uitvoerbare secties met jump-visualisaties en syntax highlighting:

`objdump {{[-d|--disassemble]}} {{pad/naar/binary}} --visualize-jumps={{color|extended-color}} --disassembler-color={{color|extended-color}}`

- Toon de symbool[t]abel:

`objdump {{[-t|--syms]}} {{pad/naar/binary}}`

- Toon een complete binary hex dump van alle [s]ecties:

`objdump {{[-s|--full-contents]}} {{pad/naar/binary}}`
