# monodis

> Mono Common Intermediar Language (CIL) dezasamblare.
> Mai multe informaţii: <https://www.mono-project.com/docs/tools+libraries/tools/monodis/>

- Dezasamblați un ansamblu la CIL textual:

`monodis {{path/to/assembly.exe}}`

- Salvați ieșirea într-un fișier:

`monodis --output={{path/to/output.il}} {{path/to/assembly.exe}}`

- Afișați informații despre un ansamblu:

`monodis --assembly {{path/to/assembly.dll}}`

- Listați referințele unei adunări:

`monodis --assemblyref {{path/to/assembly.exe}}`

- Listați toate metodele într-un ansamblu:

`monodis --method {{path/to/assembly.exe}}`

- Afișează o listă de resurse încorporate într-un ansamblu:

`monodis --manifest {{path/to/assembly.dll}}`

- Extrageți toate resursele încorporate în directorul curent:

`monodis --mresources {{path/to/assembly.dll}}`
