# delta

> Git és diff kimenetek megjelenítője. További információ: <https://github.com/dandavison/delta>.

- Fájlok vagy könyvtárak összehasonlítása:

`delta {{path/to/old_file_or_directory}} {{path/to/new_file_or_directory}}`

- Fájlok vagy könyvtárak összehasonlítása a sorszámok megjelenítésével:

`delta --line-numbers {{path/to/old_file_or_directory}} {{path/to/new_file_or_directory}}`

- Fájlok vagy könyvtárak összehasonlítása, a különbségek egymás melletti megjelenítése:

`delta --side-by-side {{path/to/old_file_or_directory}} {{path/to/new_file_or_directory}}`

- Fájlok vagy könyvtárak összehasonlítása, figyelmen kívül hagyva a Git konfigurációs beállításokat:

`delta --no-gitconfig {{path/to/old_file_or_directory}} {{path/to/new_file_or_directory}}`

- Összehasonlítás, a commit hash-ok, fájlnevek és sorszámok hiperhivatkozásként való megjelenítése a terminál emulátorok hiperhivatkozási specifikációjának megfelelően:

`delta --hyperlinks {{path/to/old_file_or_directory}} {{path/to/new_file_or_directory}}`

- Az aktuális beállítások megjelenítése:

`delta --show-config`

- Támogatott nyelvek és a hozzájuk tartozó fájlkiterjesztések megjelenítése:

`delta --list-languages`
