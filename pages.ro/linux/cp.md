# cp

> Copiați fișiere și directoare.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/cp>

- Copiați un fișier în altă locație:

`cp {{path/to/source_file.ext}} {{path/to/target_file.ext}}`

- Copiați un fișier într-un alt director, păstrând numele fișierului:

`cp {{path/to/source_file.ext}} {{path/to/target_parent_directory}}`

- copiați recursiv conținutul unui director într-o altă locație (dacă destinația există, directorul este copiat în interiorul acestuia):

`cp -r {{path/to/source_directory}} {{path/to/target_directory}}`

- Copiați un director recursiv, în modul detaliat (afișează fișierele pe măsură ce acestea sunt copiate):

`cp -vr {{path/to/source_directory}} {{path/to/target_directory}}`

- Copiați fișiere text într-o altă locație, în modul interactiv (solicită utilizatorului înainte de suprascriere):

`cp -i {{*.txt}} {{path/to/target_directory}}`

- Urmați link-uri simbolice înainte de copiere:

`cp -L {{link}} {{path/to/target_directory}}`

- Utilizați calea completă a fișierelor sursă, creând toate directoarele intermediare lipsă atunci când copiați:

`cp --parents {{source/path/to/file}} {{path/to/target_file}}`
