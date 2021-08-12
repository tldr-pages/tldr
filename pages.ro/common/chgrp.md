# chgrp

> Modificați proprietatea grupului asupra fișierelor și directoarelor.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/chgrp>

- Schimbați grupul de proprietari al unui fișier/director:

`chgrp {{group}} {{path/to/file_or_directory}}`

- Modificați recursiv grupul de proprietari al unui director și conținutul acestuia:

`chgrp -R {{group}} {{path/to/directory}}`

- Schimbați grupul de proprietari al unei legături simbolice:

`chgrp -h {{group}} {{path/to/symlink}}`

- Modificați grupul de proprietari al unui fișier/director pentru a se potrivi cu un fișier de referință:

`chgrp --reference={{path/to/reference_file}} {{path/to/file_or_directory}}`
