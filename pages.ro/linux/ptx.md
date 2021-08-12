# ptx

> Generați un index permutat de cuvinte dintr-unul sau mai multe fișiere text.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/ptx>

- Generează un indice permutat în cazul în care primul câmp al fiecărei linii este o referință index:

`ptx --references {{path/to/file}}`

- Generați un index permutat cu referințe de index generate automat:

`ptx --auto-reference {{path/to/file}}`

- Generează un indice permutat cu o lățime fixă:

`ptx --width={{width_in_columns}} {{path/to/file}}`

- Generați un index permutat cu o listă de cuvinte filtrate:

`ptx --only-file={{path/to/filter}} {{path/to/file}}`

- Generează un indice permutat cu comportamente în stil SYSV:

`ptx --traditional {{path/to/file}}`
