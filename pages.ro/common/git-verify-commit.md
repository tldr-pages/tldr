# git verify-commit

> Verificați verificarea GPG a angajărilor.
> Dacă nu se verifică nicio angajare, nimic nu va fi imprimat, indiferent de opțiunile specificate.
> Mai multe informaţii: <https://git-scm.com/docs/git-verify-commit>

- Verificați dacă se angajează o semnătură GPG:

`git verify-commit {{commit_hash1 optional_commit_hash2 ...}}`

- Verificați angajamente pentru o semnătură GPG și afișați detalii despre fiecare comitere:

`git verify-commit {{commit_hash1 optional_commit_hash2 ...}} --verbose`

- Verificați dacă se angajează o semnătură GPG și imprimați detaliile brute:

`git verify-commit {{commit_hash1 optional_commit_hash2 ...}} --raw`
