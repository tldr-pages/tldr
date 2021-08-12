# git check-ref-format

> Verifică dacă un renume dat este acceptabil și iese cu o stare diferită de zero, dacă nu este.
> Mai multe informaţii: <https://git-scm.com/docs/git-check-ref-format>

- Verificați formatul renumelui specificat:

`git check-ref-format {{refs/head/refname}}`

- Imprimați numele ultimei sucursale verificate:

`git check-ref-format --branch @{-1}`

- Normalizarea unui renume:

`git check-ref-format --normalize {{refs/head/refname}}`
