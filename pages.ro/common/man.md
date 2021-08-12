# man

> Formatați și afișați paginile manuale.
> Mai multe informaţii: <https://www.man7.org/linux/man-pages/man1/man.1.html>

- Afișează pagina om pentru o comandă:

`man {{command}}`

- Afișează pagina de om pentru o comandă din secțiunea 7:

`man {{command}}.{{7}}`

- Afișează calea căutată pentru pagini de personal:

`man --path`

- Afișați locația unei pagini de manpage, mai degrabă decât a manpage în sine:

`man -w {{command}}`

- Afișează pagina de om folosind o anumită locație:

`man {{command}} --locale={{locale}}`

- Căutați pagini de lucru care conțin un șir de căutare:

`man -k "{{search_string}}"`
