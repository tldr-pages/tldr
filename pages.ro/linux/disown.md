# disown

> Permiteți subproceselor să trăiască dincolo de shell-ul la care sunt atașate.
> A se vedea, de asemenea, comanda `jobs`.
> Mai multe informaţii: <https://www.gnu.org/software/bash/manual/bash.html#index-disown>

- Renega slujba actuala:

`disown`

- Renega un anumit loc de muncă:

`disown %{{job_number}}`

- Renega toate slujbele:

`disown -a`

- Păstrați locul de muncă (nu-l renega), dar marcați-l astfel încât nici un viitor SIGHUP nu este primit la ieșirea shell:

`disown -h %{{job_number}}`
