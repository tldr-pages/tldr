# cppclean

> Trova codice inutilizzato in progetti C++.
> Maggiori informazioni: <https://github.com/myint/cppclean>.

- Esegui nella directory di un progetto:

`cppclean {{percorso/della/directory_progetto}}`

- Esegui su di un progetto dove gli header sono nella directory "inc1" ed "inc2":

`cppclean {{percorso/della/directory_progetto}} --include-path={{inc1}} --include-path={{inc2}}`

- Esegui su di uno specifico file `main.cpp`:

`cppclean {{main.cpp}}`

- Esegui della directory corrente, escludendo la directory "build":

`cppclean {{.}} --exclude={{build}}`
