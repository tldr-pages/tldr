# git daemon

> Un server foarte simplu pentru depozitele Git.
> Mai multe informaţii: <https://git-scm.com/docs/git-daemon>

- Lansați un daemon Git cu un set de directoare pe lista albă:

`git daemon --export-all {{path/to/directory1}} {{path/to/directory2}}`

- Lansați un daemon Git cu un director de bază specific și permiteți tragerea din toate subdirectoarele care arată ca depozitele Git:

`git daemon --base-path={{path/to/directory}} --export-all --reuseaddr`

- Lansați un daemon Git pentru directorul specificat, tipăriți verbal mesaje jurnal și permițând clienților Git să scrie la el:

`git daemon {{path/to/directory}} --enable=receive-pack --informative-errors --verbose`
