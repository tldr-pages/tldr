# ln

> Crea un collegamento a un file o a una directory.

- Crea un collegamento simbolico a un file (o directory):

`ln -s {{percorso/al/file}} {{percorso/al/collegamento}}`

- Sovrascrivi un collegamento esistente in modo che punti a un nuovo file:

`ln -sg {{percorso/al/nuovo/file}} {{percorso/al/collegamento}}`

- Crea un collegamento fisico a un file:

`ln {{percorso/al/file}} {{percorso/al/collegamento}}`
