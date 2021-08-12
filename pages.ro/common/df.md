# df

> Oferă o prezentare generală a utilizării spaţiului pe disc în sistemul de fişiere.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/df>

- Afișează toate sistemele de fișiere și utilizarea lor de disc:

`df`

- Afișează toate sistemele de fișiere și utilizarea lor de disc în formă lizibilă umană:

`df -h`

- Afișează sistemul de fișiere și utilizarea discului care conține fișierul sau directorul dat:

`df {{path/to/file_or_directory}}`

- Afișează statistici privind numărul de inode libere:

`df -i`

- Afișează sisteme de fișiere, dar exclud tipurile specificate:

`df -x {{squashfs}} -x {{tmpfs}}`
