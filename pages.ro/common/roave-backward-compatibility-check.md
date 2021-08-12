# roave-backward-compatibility-check

> Un instrument care poate fi utilizat pentru a verifica întreruperile de compatibilitate inversă între două versiuni ale unei biblioteci PHP.
> Mai multe informaţii: <https://github.com/Roave/BackwardCompatibilityCheck>

- Verificați dacă modificările de rupere de la ultima etichetă:

`roave-backward-compatibility-check`

- Verificați dacă modificările de rupere de la o anumită etichetă:

`roave-backward-compatibility-check --from={{git_reference}}`

- Verificați dacă există modificări de rupere între ultima etichetă și o referință specifică:

`roave-backward-compatibility-check --to={{git_reference}}`

- Verificați dacă modificările de rupere și ieșirea la Markdown:

`roave-backward-compatibility-check --format=markdown > {{results.md}}`
