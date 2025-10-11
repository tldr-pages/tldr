# readarray

> Lees regels van `stdin` in een array.
> Meer informatie: <https://www.gnu.org/software/bash/manual/bash.html#index-readarray>.

- Interactief regels in een array invoeren:

`readarray {{array_naam}}`

- Lees regels uit een bestand en plaats ze in een array:

`readarray < {{pad/naar/bestand.txt}} {{array_naam}}`

- Verwijder scheidingstekens aan het einde (standaard newline):

`readarray < {{pad/naar/bestand.txt}} -t {{array_naam}}`

- Kopieer maximaal het opgegeven aantal regels:

`readarray < {{pad/naar/bestand.txt}} -n {{N}} {{array_naam}}`

- Toon de help:

`help mapfile`
