# stack

> Instrument pentru gestionarea proiectelor Haskell.
> Mai multe informaţii: <https://github.com/commercialhaskell/stack>

- Creați un pachet nou:

`stack new {{package_name}} {{template_name}}`

- Compilarea unui pachet:

`stack build`

- Executați teste în interiorul unui pachet:

`stack test`

- Compilați un proiect și recompilați de fiecare dată când se modifică un fișier:

`stack build --file-watch`

- Compilarea unui proiect și executarea unei comenzi după compilare:

`stack build --exec "{{command}}"`

- Rulați un program și transmiteți un argument:

`stack exec {{program_name}} -- {{argument}}`
