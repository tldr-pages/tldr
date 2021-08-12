# tokei

> Un program care imprimă statistici despre cod.
> Mai multe informaţii: <https://github.com/XAMPPRocky/tokei>

- Obțineți un raport privind codul într-un director și toate subdirectoarele:

`tokei {{path/to/directory}}`

- Obțineți un raport pentru un director cu excepția fișierelor `.min.js`:

`tokei {{path/to/directory}} -e {{*.min.js}}`

- Tipăriți statistici pentru fișiere individuale într-un director:

`tokei {{path/to/directory}} --files`

- Obțineți un raport pentru toate fișierele de tip Rust și Markdown:

`tokei {{path/to/directory}} -t={{Rust}},{{Markdown}}`
