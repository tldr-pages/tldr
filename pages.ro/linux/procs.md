# procs

> Afișați informații despre procesele active.
> Mai multe informaţii: <https://github.com/dalance/procs>

- Listează toate procesele care arată PID, utilizator, utilizarea procesorului, utilizarea memoriei și comanda care le-a pornit:

`procs`

- Afișați informații despre procese, dacă comenzile care au început conțin `zsh`:

`procs {{zsh}}`

- Afișați informații despre toate procesele sortate după timpul procesorului în ordinea [a] scending sau [d] escending:

`procs {{--sortd|--sorta}} cpu`

- Afișați informații despre procesele cu un PID, o comandă sau un utilizator care conține (`zsh` sau `firefox`):

`procs --or {{PID|command|user}} {{41}} {{firefox}}`

- Afișați informații despre procesele cu PID `41` și o comandă sau un utilizator care conține `zsh`:

`procs --and {{41}} {{zsh}}`
