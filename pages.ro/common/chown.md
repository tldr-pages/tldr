# chown

> Modificați proprietatea utilizatorilor și a grupului asupra fișierelor și directoarelor.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/chown>

- Schimbați utilizatorul proprietarului unui fișier/director:

`chown {{user}} {{path/to/file_or_directory}}`

- Schimbați utilizatorul proprietar și grupul unui fișier/director:

`chown {{user}}:{{group}} {{path/to/file_or_directory}}`

- Modificarea recursivă a proprietarului unui director și a conținutului acestuia:

`chown -R {{user}} {{path/to/directory}}`

- Schimbați proprietarul unei legături simbolice:

`chown -h {{user}} {{path/to/symlink}}`

- Modificați proprietarul unui fișier/director pentru a se potrivi cu un fișier de referință:

`chown --reference={{path/to/reference_file}} {{path/to/file_or_directory}}`
