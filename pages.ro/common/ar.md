# ar

> Crearea, modificarea și extragerea din arhive (`.a`, `.so`, `.o`).
> Mai multe informaţii: <https://manned.org/ar>

- Extrageţi toţi membrii dintr-o arhivă:

`ar -x {{path/to/file.a}}`

- Lista membrilor unei arhive:

`ar -t {{path/to/file.a}}`

- Înlocuiți sau adăugați fișiere într-o arhivă:

`ar -r {{path/to/file.a}} {{path/to/file1.o}} {{path/to/file2.o}}`

- Inserați un index de fișier obiect (echivalent cu utilizarea `ranlib`):

`ar -s {{path/to/file.a}}`

- Creați o arhivă cu fișiere și un index de fișier obiect însoțitor:

`ar -rs {{path/to/file.a}} {{path/to/file1.o}} {{path/to/file2.o}}`
