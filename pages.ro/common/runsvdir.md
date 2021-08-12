# runsvdir

> Rulați un întreg director de servicii.
> Mai multe informaţii: <https://manpages.ubuntu.com/manpages/latest/man8/runsvdir.8.html>

- Porniți și gestionați toate serviciile într-un director ca utilizator curent:

`runsvdir {{path/to/services}}`

- Porniți și gestionați toate serviciile într-un director ca root:

`sudo runsvdir {{path/to/services}}`

- Începeți serviciile în sesiuni separate:

`runsvdir -P {{path/to/services}}`
