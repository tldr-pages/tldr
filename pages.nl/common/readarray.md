# readarray

> Lees regels van `stdin` in een array.
> Meer informatie: <https://www.gnu.org/software/bash/manual/bash.html#index-readarray>.

- Interactief regels in een array invoeren:

`readarray {{array_naam}}`

- Lees regels uit een bestand en plaats ze in een array:

`readarray {{array_naam}} < {{pad/naar/bestand.txt}}`

- Verwijder scheidingstekens aan het einde (standaard newline):

`readarray -t {{array_naam}} < {{pad/naar/bestand.txt}}`

- Kopieer maximaal het opgegeven aantal regels:

`readarray -n {{N}} {{array_naam}} < {{pad/naar/bestand.txt}}`

- Toon de help:

`help mapfile`
