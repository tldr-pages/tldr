# ln

> Crea un collegamento a un file o a una cartella.
> Maggiori informazioni: <https://www.gnu.org/software/coreutils/ln>.

- Crea un collegamento simbolico a un file (o cartella):

`ln -s {{/percorso/al/file}} {{percorso/al/collegamento}}`

- Sovrascrivi un collegamento esistente in modo che punti a un nuovo file:

`ln -sf {{/percorso/al/nuovo/file}} {{percorso/al/collegamento}}`

- Crea un collegamento fisico a un file:

`ln {{/percorso/al/file}} {{percorso/al/collegamento}}`
