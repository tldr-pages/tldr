# gunzip

> Extrageţi fişiere dintr-o arhivă gzip (.gz).
> Mai multe informaţii: <https://manned.org/gunzip>

- Extrageți un fișier dintr-o arhivă, înlocuind fișierul original dacă acesta există:

`gunzip {{archive.tar.gz}}`

- Extrageţi un fişier la o destinaţie ţintă:

`gunzip --stdout {{archive.tar.gz}} > {{archive.tar}}`

- Extrageţi un fişier şi păstraţi fişierul de arhivă:

`gunzip --keep {{archive.tar.gz}}`

- Listați conținutul unui fișier comprimat:

`gunzip --list {{file.txt.gz}}`
