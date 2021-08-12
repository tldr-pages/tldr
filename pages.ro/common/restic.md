# restic

> Un program de backup care își propune să fie rapid, sigur și eficient.
> Mai multe informaţii: <https://restic.net>

- Inițializați un depozit de rezervă în directorul local specificat:

`restic init --repo {{path/to/repository}}`

- Copierea de rezervă a unui director în depozit:

`restic --repo {{path/to/repository}} backup {{path/to/directory}}`

- Afișează instantaneele de rezervă stocate în prezent în depozit:

`restic --repo {{path/to/repository}} snapshots`

- Restaurați un instantaneu de rezervă specific într-un director țintă:

`restic --repo {{path/to/repository}} restore {{latest|snapshot_id}} --target {{path/to/target}}`

- Restaurați o anumită cale dintr-o copie de rezervă specifică într-un director țintă:

`restic --repo {{path/to/repository}} restore {{snapshot_id}} --target {{path/to/target}} --include {{path/to/restore}}`

- Curățați depozitul și păstrați doar cel mai recent instantaneu al fiecărui backup unic:

`restic forget --keep-last 1 --prune`
