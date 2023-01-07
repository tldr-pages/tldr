# ln

> Crea un collegamento a un file o a una directory.
> Maggiori informazioni: <https://www.gnu.org/software/coreutils/ln>.

- Crea un collegamento simbolico a un file (o directory):

`ln -s {{/percorso/del/file}} {{percorso/del/collegamento}}`

- Sovrascrivi un collegamento esistente in modo che punti a un nuovo file:

`ln -sf {{/percorso/del/nuovo/file}} {{percorso/del/collegamento}}`

- Crea un collegamento fisico a un file:

`ln {{/percorso/del/file}} {{percorso/del/collegamento}}`
