# pax

> Utilitar de arhivare și copiere.

- Listează conținutul unei arhive:

`pax -f {{archive.tar}}`

- Listează conținutul unei arhive gzipped:

`pax -zf {{archive.tar.gz}}`

- Creați o arhivă din fișiere:

`pax -wf {{target.tar}} {{path/to/file1}} {{path/to/file2}} {{path/to/file3}}`

- Creați o arhivă din fișiere, utilizând redirecționarea ieșirii:

`pax -w {{path/to/file1}} {{path/to/file2}} {{path/to/file3}} > {{target.tar}}`

- Extrageţi o arhivă în directorul curent:

`pax -rf {{source.tar}}`

- Copiați într-un director, păstrând în același timp metadatele originale; `țintă/` trebuie să existe:

`pax -rw {{path/to/file1}} {{path/to/directory1}} {{path/to/directory2}} {{target/}}`
