# disown

> Permite que los subprocesos sigan activos más allá del intérprete de comandos al que están vinculados.
Vea también: `jobs`.
> Más información: <https://www.gnu.org/software/bash/manual/bash.html#index-disown>.

- Renuncia al trabajo actual:

`disown`

- Renuncia a un trabajo específico (ejecute `jobs` para encontrar el número de trabajo):

`disown %{{número_trabajo}}`

- Renuncia a todos los trabajos (solo Bash):

`disown -a`

- Mantiene el trabajo (no renuncia a él), pero lo marca para que no se reciba ningún SIGHUP futuro al salir del intérprete de comandos (solo Bash):

`disown -h %{{jnúmero_trabajo}}`
