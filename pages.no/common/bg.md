# bg

> Gjenopptar jobber som er suspendert (f.eks. ved hjelp av `<Ctrl z>`), og holder dem i gang i bakgrunnen.
> Mer informasjon: <https://www.gnu.org/software/bash/manual/bash.html#index-bg>.

- Gjenoppta den sist suspenderte jobben og kjør den i bakgrunnen:

`bg`

- Gjenoppta en spesifikk jobb (bruk `jobs -l` for å finne riktig ID) og kjør den i bakgrunnen:

`bg %{{jobb_id}}`
