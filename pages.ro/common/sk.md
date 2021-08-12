# sk

> Fuzzy Finder scris în Rust.
> Similar cu `fzf`.
> Mai multe informaţii: <https://github.com/lotabout/skim>

- Începeți degresarea pe toate fișierele din directorul specificat:

`find {{path/to/directory}} -type f | sk`

- Porniți degresare pentru procesele de funcționare:

`ps aux | sk`

- Începeți degresarea cu o interogare specificată:

`sk --query "{{query}}"`

- Selectați mai multe fișiere cu `Shift + Tab` și scrieți într-un fișier:

`find {{path/to/directory}} -type f | sk --multi > {{filename}}`
