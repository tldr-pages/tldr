# mv

> Sposta o rinomina file e directory.
> Maggiori informazioni: <https://www.gnu.org/software/coreutils/mv>.

- Sposta file:

`mv {{sorgente}} {{destinazione}}`

- Sposta file senza chiedere conferma prima di sovrascrivere file esistenti:

`mv -f {{sorgente}} {{destinazione}}`

- Sposta file interattivamente, chiedendo conferma prima di sovrascrivere file esistenti:

`mv -i {{sorgente}} {{destinazione}}`

- Sposta file senza sovrascrivere file esistenti:

`mv -n {{sorgente}} {{destinazione}}`

- Sposta file in modalità verbosa, mostrando a schermo ogni file che viene spostato:

`mv -v {{sorgente}} {{destinazione}}`
