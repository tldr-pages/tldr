# namei

> Urmează un nume de cale (care poate fi o legătură simbolică) până când se găsește un punct terminal (un fișier/director/dispozitiv char etc.).
> Acest program este util pentru a găsi „prea multe niveluri de link-uri simbolice” probleme.

- Rezolvarea numelor de căi specificate ca parametri de argument:

`namei {{path/to/a}} {{path/to/b}} {{path/to/c}}`

- Afișați rezultatele într-un format de listare lungă:

`namei --long {{path/to/a}} {{path/to/b}} {{path/to/c}}`

- Afișează biții de mod din fiecare tip de fișier în stilul `ls`:

`namei --modes {{path/to/a}} {{path/to/b}} {{path/to/c}}`

- Arată numele proprietarului și al grupului fiecărui fișier:

`namei --owners {{path/to/a}} {{path/to/b}} {{path/to/c}}`

- Nu urmați linkurile simbolice în timp ce rezolvați:

`namei --nosymlinks {{path/to/a}} {{path/to/b}} {{path/to/c}}`
