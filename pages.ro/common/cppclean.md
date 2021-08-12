# cppclean

> Găsiți codul neutilizat în proiectele C++.
> Mai multe informaţii: <https://github.com/myint/cppclean>

- Rulați în directorul unui proiect:

`cppclean {{path/to/project}}`

- Rulați pe un proiect în care anteturile sunt în directoarele „inc1/” și „inc2/”:

`cppclean {{path/to/project}} --include-path={{inc1}} --include-path={{inc2}}`

- Rulați pe un anumit fișier `main.cpp`:

`cppclean {{main.cpp}}`

- Rulați pe directorul curent, excluzând directorul „build”:

`cppclean {{.}} --exclude={{build}}`
