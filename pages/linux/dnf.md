# dnf

> Package management utility for RHEL, Fedora, and CentOS (replaces yum).

- Synchronize list of packages and versions available. This should be run first, before running subsequent dnf commands:

`dnf update`

- Install a new package:

`dnf install {{package}}`

- Install a new package and assume yes to all questions:

`dnf -y install {{package}}`

- Remove a package:

`dnf remove {{package}}`

- Upgrade installed packages to newest available versions:

`dnf upgrade`
