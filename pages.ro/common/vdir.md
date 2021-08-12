# vdir

> Listează conținutul directorului.
> Înlocuire drop-in pentru `l-l`.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/vdir>

- Lista fișierelor și directoarelor din directorul curent, câte unul pe rând, cu detalii:

`vdir`

- Lista cu dimensiunile afișate în unități lizibile umane (KB, MB, GB):

`vdir -h`

- Listă inclusiv fișiere ascunse (începând cu un punct):

`vdir -a`

- Lista fișierelor și directoarelor de sortare a intrărilor după dimensiune (prima cea mai mare):

`vdir -S`

- Lista fișierelor și directoarelor de sortare a intrărilor după momentul modificării (cel mai nou primul):

`vdir -t`

- Lista directoarelor de grupare mai întâi:

`vdir --group-directories-first`

- Lista recursivă a tuturor fișierelor și directoarelor într-un anumit director:

`vdir --recursive {{path/to/directory}}`
