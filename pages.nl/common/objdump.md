# objdump

> Bekijk informatie over object bestanden.
> Meer informatie: <https://manned.org/objdump>.

- Toon de bestand header informatie:

`objdump -f {{binary}}`

- Toon alle header informatie:

`objdump -x {{binary}}`

- Toon de gedemonteerde uitvoer van uitvoerbare secties:

`objdump -d {{binary}}`

- Toon de gedemonteerde uitvoer van uitvoerbare secties in intel syntax:

`objdump -M intel -d {{binary}}`

- Toon een complete binary hex dump van alle secties:

`objdump -s {{binary}}`
