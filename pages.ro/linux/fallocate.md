# fallocate

> Rezervă sau distribuiți spațiu pe disc pentru fișiere.
> Utilitarul alocă spațiu fără zero.
> Mai multe informaţii: <https://manned.org/fallocate>

- Rezervă un fișier care ocupă 700MB de spațiu pe disc:

`fallocate --length {{700M}} {{path/to/file}}`

- Micșorați un fișier deja alocat cu 200MB:

`fallocate --collapse-range --length {{200M}} {{path/to/file}}`

- Micșorați 20 MB de spațiu după 100MB într-un fișier:

`fallocate --collapse-range --offset {{100M}} --length {{20M}} {{path/to/file}}`
