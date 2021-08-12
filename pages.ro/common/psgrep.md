# psgrep

> Caută procese care rulează cu `grep`.
> Mai multe informaţii: <https://jvz.github.io/psgrep>

- Găsiți linii de proces care conțin un șir specific:

`psgrep {{process_name}}`

- Găsiți linii de proces care conțin un șir specific, excluzând anteturile:

`psgrep -n {{process_name}}`

- Căutare utilizând un format simplificat (PID, utilizator, comandă):

`psgrep -s {{process_name}}`
