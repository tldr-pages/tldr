# rmlint

> Identify duplicate files or directories, and other filesystem issues.
> More information: <https://rmlint.readthedocs.io/en/latest/rmlint.1.html>.

- Check directory for duplicates, empty files, and other lint:

`rmlint {{path/to/directory}}`

- Delete lint files found by an rmlint run:

`./rmlint.sh`

- Find all duplicates with the same base name:

`rmlint --match-basename {{path/to/directory}}`

- Find all duplicates with the same extension:

`rmlint --match-extension {{path/to/directory}}`
