# git verify-tag

> Verificați dacă există verificarea GPG a etichetelor.
> Dacă o etichetă nu a fost semnată, va apărea o eroare.
> Mai multe informaţii: <https://git-scm.com/docs/git-verify-tag>

- Verificați etichetele pentru o semnătură GPG:

`git verify-tag {{tag1 optional_tag2 ...}}`

- Verificați etichetele pentru o semnătură GPG și afișați detalii pentru fiecare etichetă:

`git verify-tag {{tag1 optional_tag2 ...}} --verbose`

- Verificați etichetele pentru o semnătură GPG și imprimați detaliile brute:

`git verify-tag {{tag1 optional_tag2 ...}} --raw`
