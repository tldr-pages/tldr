# dnf changelog

> View the changelogs for a given package.
> Not default to `dnf` but supported via `dnf-plugins-core`.
> See also: `dnf`.
> More information: <https://dnf-plugins-core.readthedocs.io/en/latest/changelog.html>.

- View all changelogs for a given package:

`dnf changelog {{path/to/specification.spec}}`

- View all changelogs for a given package after a specified date:

`dnf changelog --since {{date}} {{path/to/specification.spec}}`

- View the last `n` number of changelogs for a given package:

`dnf changelog --count {{number}} {{path/to/specification.spec}}`

- Show only new items for upgradeable packages:

`dnf changelog --upgrades {{path/to/specification.spec}}`

- Display help:

`dnf changelog --help-cmd`
