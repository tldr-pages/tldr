# srm

> Eliminați în siguranță fișierele sau directoarele.
> Suprascrie datele existente de una sau de mai multe ori. Înlocuirea înlocuitorului pentru rm.
> Mai multe informaţii: <http://srm.sourceforge.net/srm.html>

- Eliminați un fișier după o suprascriere unică cu date aleatorii:

`srm -s {{path/to/file}}`

- Eliminați un fișier după șapte treceri de suprascriere cu date aleatorii:

`srm -m {{path/to/file}}`

- Eliminați recursiv un director și conținutul său suprascrie fiecare fișier cu o singură trecere de date aleatoare:

`srm -r -s {{path/to/directory}}`

- Prompt înainte de fiecare eliminare:

`srm -i {{\*}}`
