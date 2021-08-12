# ln

> Creează linkuri către fișiere și directoare.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/ln>

- Creați un link simbolic către un fișier sau director:

`ln -s {{/path/to/file_or_directory}} {{path/to/symlink}}`

- Suprascrie un link simbolic existent pentru a indica spre un alt fișier:

`ln -sf {{/path/to/new_file}} {{path/to/symlink}}`

- Creați un link dur către un fișier:

`ln {{/path/to/file}} {{path/to/hardlink}}`
