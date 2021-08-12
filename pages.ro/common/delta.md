# delta

> Un vizualizator pentru ieșire Git și diff.
> Mai multe informaţii: <https://github.com/dandavison/delta>

- Comparați fișiere sau directoare:

`delta {{path/to/old_file_or_directory}} {{path/to/new_file_or_directory}}`

- Comparați fișiere sau directoare, arătând numerele de linie:

`delta --line-numbers {{path/to/old_file_or_directory}} {{path/to/new_file_or_directory}}`

- Comparați fișierele sau directoarele, arătând diferențele una lângă alta:

`delta --side-by-side {{path/to/old_file_or_directory}} {{path/to/new_file_or_directory}}`

- Comparați fișierele sau directoarele, ignorând orice setări de configurare Git:

`delta --no-gitconfig {{path/to/old_file_or_directory}} {{path/to/new_file_or_directory}}`

- Comparați, randați hash-uri comite, nume de fișiere și numere de linie ca hyperlink-uri, în funcție de specificația hyperlink pentru emulatori terminale:

`delta --hyperlinks {{path/to/old_file_or_directory}} {{path/to/new_file_or_directory}}`

- Afișează setările curente:

`delta --show-config`

- Afișați limbile acceptate și extensiile de fișiere asociate:

`delta --list-languages`
