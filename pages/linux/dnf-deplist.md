# dnf deplist

> Show the dependency tree of a package.
> Note: DNF5 removed `dnf deplist` and `dnf repoquery --deplist`. Use `dnf deptree`.
> More information: <https://dnf5.readthedocs.io/en/latest/dnf5_plugins/deptree.8.html>.

- Show the dependency tree of a package:

`dnf deptree {{package}}`

- Show the tree using installed packages only:

`dnf deptree --installed {{package}}`

- Show packages that depend on a package:

`dnf deptree --reverse {{package}}`

- Print a flat list of dependencies:

`dnf deptree --flat {{package}}`
