# nim

> Compilatorul Nim.
> Procese, compilează și leagă fișierele sursă de limbă Nim.
> Mai multe informaţii: <https://nim-lang.org>

- Compilarea unui fișier sursă:

`nim compile {{file.nim}}`

- Compilarea și rularea unui fișier sursă:

`nim compile -r {{file.nim}}`

- Compilați un fișier sursă cu optimizări de lansare activate:

`nim compile -d:release {{file.nim}}`

- Construiți un binar de lansare optimizat pentru dimensiunea redusă a fișierului:

`nim compile -d:release --opt:size {{file.nim}}`

- Generarea documentației HTML pentru un modul (ieșirea va fi plasată în directorul curent):

`nim doc {{file.nim}}`
