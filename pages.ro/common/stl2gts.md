# stl2gts

> Conversia fișierelor STL în formatul de fișier GTS (bibliotecă de suprafață triangulată GNU).
> Mai multe informaţii: <https://manned.org/stl2gts>

- Conversia unui fişier STL într-un fişier GTS:

`stl2gts  <{{path/to/file.stl}}> {{path/to/file.gts}}`

- Conversia unui fișier STL într-un fișier GTS și revenirea normală față:

`stl2gts --revert  <{{path/to/file.stl}}> {{path/to/file.gts}}`

- Conversia unui fișier STL într-un fișier GTS și nu îmbinați vârfurile:

`stl2gts --nomerge  <{{path/to/file.stl}}> {{path/to/file.gts}}`

- Conversia unui fișier STL într-un fișier GTS și afișarea statisticilor de suprafață:

`stl2gts --verbose  <{{path/to/file.stl}}> {{path/to/file.gts}}`

- Ajutor de imprimare pentru `stl2gts`:

`stl2gts --help`
