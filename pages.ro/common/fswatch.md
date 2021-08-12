# fswatch

> Un monitor de schimbare a fişierelor inter-platformă.
> Mai multe informaţii: <https://emcrisostomo.github.io/fswatch>

- Rulați o comandă bash la crearea, actualizarea sau ștergerea fișierelor:

`fswatch {{path/to/file}} | xargs -n 1 {{bash_command}}`

- Urmăriți unul sau mai multe fișiere și/sau directoare:

`fswatch {{path/to/file}} {{path/to/directory}} {{path/to/another_directory/**/*.js}} | xargs -n 1 {{bash_command}}`

- Imprimați căile absolute ale fișierelor modificate:

`fswatch {{path/to/directory}} | xargs -n 1 -I {} echo {}`

- Filtrează după tipul evenimentului, de exemplu. Actualizat, șters sau creat:

`fswatch --event {{Updated}} {{path/to/directory}} | xargs -n 1 {{bash_command}}`
