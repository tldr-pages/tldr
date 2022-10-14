# cppclean

> Trova codice inutilizzato in progetti C++.
> Maggiori informazioni: <https://github.com/myint/cppclean>.

- Esegui nella cartella di un progetto:

`cppclean {{percorso/a/cartella_progetto}}`

- Esegui su di un progetto dove gli header sono nella cartella "inc1" ed "inc2":

`cppclean {{percorso/a/cartella_progetto}} --include-path={{inc1}} --include-path={{inc2}}`

- Esegui su di uno specifico file `main.cpp`:

`cppclean {{main.cpp}}`

- Esegui della cartella corrente, escludendo la cartella "build":

`cppclean {{.}} --exclude={{build}}`
