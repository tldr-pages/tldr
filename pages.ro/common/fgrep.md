# fgrep

> Potrivește tiparele din fișiere.
> Suportă modele simple și expresii regulate.
> Mai multe informaţii: <https://manned.org/fgrep>

- Căutați un șir exact într-un fișier:

`fgrep {{search_string}} {{path/to/file}}`

- Căutați numai linii care se potrivesc în întregime în fișiere:

`fgrep -x {{path/to/file1}} {{path/to/file2}}`

- Numără numărul de linii care se potrivesc cu șirul dat într-un fișier:

`fgrep -c {{search_string}} {{path/to/file}}`

- Afișați numărul liniei din fișier împreună cu linia potrivită:

`fgrep -n {{search_string}} {{path/to/file}}`

- Afișează toate liniile, cu excepția celor care conțin expresia regulată dată:

`fgrep -v {{regular_expression}} {{path/to/file}}`

- Afișează nume de fișiere al căror conținut se potrivește cu expresia regulată cel puțin o dată:

`fgrep -l {{regular_expression}} {{path/to/file1}} {{path/to/file2}}`
