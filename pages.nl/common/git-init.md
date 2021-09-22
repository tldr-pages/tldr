# git init

> Initialiseer een nieuwe lokale Git repository:
> Meer informatie: <https://git-scm.com/docs/git-init>.

- Initialiseer een nieuwe lokale repository:

`git init`

- Initialiseer een repository met een specifieke naam for de eerste branch:

`git init --initial-branch={{branch_name}}`

- Initialiseer een repository met SHA256 for object hashes (vereist Git versie 2.29 of hoger):

`git init --object-format={{sha256}}`

- Initialisser een bare-bones repository, geschikt voor gebruik over SSH:

`git init --bare`
