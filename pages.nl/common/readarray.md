# readarray

> Lees regels van `stdin` in een array.
> Meer informatie: <https://www.gnu.org/software/bash/manual/bash.html#index-readarray>.

- Interactief regels in een array invoeren:

`readarray {{array_naam}}`

- Lees regels uit een bestand en plaats ze in een array:

`readarray < {{pad/naar/bestand.txt}} {{array_naam}}`

- Verwijder scheidingstekens aan het einde ([t]) (standaard newline):

`readarray < {{pad/naar/bestand.txt}} -t {{array_naam}}`

- Kopieer maximaal `n` regels:

`readarray < {{pad/naar/bestand.txt}} -n {{n}} {{array_naam}}`

- [s]la de eerste `n` regels over:

`readarray < {{pad/naar/bestand.txt}} -s {{n}} {{array_naam}}`

- Zet een aangepast schei[d]ingsteken:

`readarray < {{path/to/file.txt}} -d {{scheidingsteken}} {{array_naam}}`

- Toon de help:

`help mapfile`
