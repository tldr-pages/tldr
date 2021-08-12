# git prune

> Comanda Git pentru tăierea tuturor obiectelor inaccesibile din baza de date obiect.
> Această comandă nu este adesea utilizată direct, ci ca o comandă internă utilizată de Git gc.
> Mai multe informaţii: <https://git-scm.com/docs/git-prune>

- Raportați ce ar fi eliminat prin prune Git fără a scoate:

`git prune --dry-run`

- Prune obiecte inaccesibile și afișa ceea ce a fost tăiat la stdout:

`git prune --verbose`

- Prune obiecte inaccesibile în timp ce arată progresul:

`git prune --progress`
