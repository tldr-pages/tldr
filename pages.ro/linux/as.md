# as

> Ansamblor GNU portabil.
> Destinate în principal asamblării producției de la `gcc` pentru a fi utilizate de către `ld`.
> Mai multe informaţii: <https://manned.org/as>

- Asamblarea unui fișier, scrierea ieșirii la `a.out`:

`as {{file.s}}`

- Asamblați ieșirea într-un fișier dat:

`as {{file.s}} -o {{out.o}}`

- Generează rezultatul mai rapid sărind peste spațiul alb și comentând preprocesarea. (Ar trebui să fie utilizate numai pentru compilatoare de încredere):

`as -f {{file.s}}`

- Includeți o cale dată către lista de directoare pentru a căuta fișiere specificate în directivele `.include`:

`as -I {{path/to/directory}} {{file.s}}`
