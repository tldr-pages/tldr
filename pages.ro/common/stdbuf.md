# stdbuf

> Executați o comandă cu operații tampon modificate pentru fluxurile sale standard.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/stdbuf>

- Modificați dimensiunea tamponului standard de intrare la 512 KiB:

`stdbuf --input={{512K}} {{command}}`

- Schimbați tamponul standard de ieșire la linia bufferată:

`stdbuf --output={{L}} {{command}}`

- Modificați bufferul de eroare standard la unbuffered:

`stdbuf --error={{0}} {{command}}`
