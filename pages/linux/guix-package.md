# guix package

> Install, upgrade and remove Guix packages, or rollback to previous configurations.
> More information: <https://guix.gnu.org/manual/html_node/Invoking-guix-package.html>.

- Install a new package:

`guix package {{[-i|--install]}} {{package}}`

- Remove a package:

`guix package {{[-r|--remove]}} {{package}}`

- Search the package database for a regular expression:

`guix package {{[-s|--search]}} "{{search_pattern}}"`

- List installed packages:

`guix package {{[-I|--list-installed]}}`

- List generations:

`guix package {{[-l|--list-generations]}}`

- Roll back to the previous generation:

`guix package --roll-back`
