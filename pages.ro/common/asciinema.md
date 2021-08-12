# asciinema

> Înregistrați și reluați sesiunile terminale și, opțional, partajați-le pe asciinema.org.
> Mai multe informaţii: <https://asciinema.org/>

- Asociați instalarea locală a `asciinema` cu un cont asciinema.org:

`asciinema auth`

- Efectuați o nouă înregistrare (odată terminată, utilizatorul va fi rugat să o încarce sau să o salveze local):

`asciinema rec`

- Faceți o înregistrare nouă și salvați-o într-un fișier local:

`asciinema rec {{path/to/file}}.cast`

- Reluarea unei înregistrări terminale dintr-un fișier local:

`asciinema play {{path/to/file}}.cast`

- Replay o înregistrare terminal găzduit pe asciinema.org:

`asciinema play https://asciinema.org/a/{{cast_id}}`

- Efectuați o nouă înregistrare, limitând orice timp de inactivitate la cel mult 2,5 secunde:

`asciinema rec -i {{2.5}}`

- Imprimați ieșirea completă a unei înregistrări salvate local:

`asciinema cat {{path/to/file}}.cast`

- Încărcați o sesiune terminală salvată local pe asciinema.org:

`asciinema upload {{path/to/file}}.cast`
