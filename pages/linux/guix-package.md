# guix package

> Install, upgrade and remove Guix packages, or rollback to previous configurations.

- Install a new package:

`guix package -i {{package_name}}`

- Remove a package:

`guix package -r {{package_name}}`

- Search the package database for a regular expression:

`guix package -s "{{search_pattern}}"`

- List installed packages:

`guix package -I`

- List generations:

`guix package -l`

- Roll back to the previous generation:

`guix package --roll-back`
