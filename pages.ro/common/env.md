# env

> Afișați mediul sau executați un program într-un mediu modificat.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/env>

- Arată mediul:

`env`

- Rulează un program. Adesea folosit în scripturi după shebang (#!) pentru a căuta calea către program:

`env {{program}}`

- Ștergeți mediul și executați un program:

`env -i {{program}}`

- Eliminați variabila din mediul înconjurător și executați un program:

`env -u {{variable}} {{program}}`

- Setați o variabilă și executați un program:

`env {{variable}}={{value}} {{program}}`

- Setați mai multe variabile și executați un program:

`env {{variable1}}={{value}} {{variable2}}={{value}} {{variable3}}={{value}} {{program}}`
